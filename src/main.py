from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET

LOG_PATH = "sample_logs/Security.evtx"

with Evtx(LOG_PATH) as log:
    for i, record in enumerate(log.records()):

        xml = record.xml()

        root = ET.fromstring(xml)

        namespace = {
            "e": "http://schemas.microsoft.com/win/2004/08/events/event"
        }

        event_id = root.find(".//e:EventID", namespace)

        if event_id is not None:
            print(event_id.text)

        if i >= 9:
            break