from Evtx.Evtx import Evtx
from collections import Counter
from detector import get_severity
from event_map import EVENT_MAP
import xml.etree.ElementTree as ET

LOG_PATH = "sample_logs/Security.evtx"
event_counter = Counter()
alert_counter = Counter()

with Evtx(LOG_PATH) as log:
    for i, record in enumerate(log.records()):
        xml = record.xml()
        root = ET.fromstring(xml)
        namespace = {
            "e": "http://schemas.microsoft.com/win/2004/08/events/event"
        }
        event_id = root.find(".//e:EventID", namespace)
        if event_id is not None:
            event_id = int(event_id.text)
            event_counter[event_id] += 1
            meaning = EVENT_MAP.get(event_id, "Unknown")
            time_node = root.find(".//e:TimeCreated", namespace)
            event_time = time_node.attrib.get("SystemTime") if time_node is not None else "Unknown Time"
            severity = get_severity(event_id)
            if severity == "ALERT":
                alert_counter[event_id] += 1
            print(f"[{severity}] {event_time} | {event_id} | {meaning}")
        if i >= 9:
            break
print("\n=== Event Summary ===")
for event_id, count in event_counter.most_common():
    meaning = EVENT_MAP.get(event_id, "Unknown")
    print(f"{event_id:<6} {meaning:<30} {count}")
print("\n=== ALERT Event Summary ===")
for event_id, count in alert_counter.most_common():
    meaning = EVENT_MAP.get(event_id, "Unknown")
    print(f"[ALERT] {event_id:<6} {meaning:<30} {count}回")