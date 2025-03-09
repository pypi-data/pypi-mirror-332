from datetime import datetime, timezone
from uuid import RFC_4122, UUID

import pytest

from hive.chat import ChatMessage, tell_user, tell_user_errors
from hive.common import parse_datetime


def test_basic_operation(mock_messagebus, mock_channel):
    tell_user("bonjour!", channel=mock_channel)

    assert len(mock_messagebus.published_events) == 1
    event = mock_messagebus.published_events[0]
    assert event.routing_key == "chat.messages"
    message = event.message

    assert message.keys() == {"text", "sender", "timestamp", "uuid"}
    assert message["text"] == "bonjour!"
    assert message["sender"] == "hive"

    timestamp = parse_datetime(message["timestamp"])
    delta = (datetime.now(tz=timezone.utc) - timestamp).total_seconds()
    assert 0 <= delta < 1

    uuid = UUID(message["uuid"])
    assert uuid.variant == RFC_4122
    assert uuid.version == 4


def test_channel_creation(mock_messagebus):
    tell_user(ChatMessage(
        text="salop!",
        timestamp="2024-11-23 10:52:19.542344Z",
        uuid="urn:uuid:0669fa00-93d8-4c35-bccc-469258b9b065",
    ))

    assert len(mock_messagebus.published_events) == 1
    event = mock_messagebus.published_events[0]
    assert event.routing_key == "chat.messages"
    assert event.message == {
        "text": "salop!",
        "sender": "hive",
        "timestamp": "2024-11-23 10:52:19.542344+00:00",
        "uuid": "0669fa00-93d8-4c35-bccc-469258b9b065",
    }


def test_tell_user_errors(mock_messagebus):
    class TestError(Exception):
        pass

    with pytest.raises(TestError):
        with tell_user_errors():
            raise TestError("oh <no>!")

    assert len(mock_messagebus.published_events) == 1
    event = mock_messagebus.published_events[0]
    assert event.routing_key == "chat.messages"
    assert event.message.keys() == {
        "text", "html", "sender", "timestamp", "uuid",
    }
    assert event.message["text"] == "TestError: oh <no>!"
    assert event.message["html"].endswith(
        " <code>TestError: oh &lt;no&gt;!</code>",
    )
