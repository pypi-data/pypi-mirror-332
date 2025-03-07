import json
import threading
import time
from io import BytesIO

import pycurl
from websocket import create_connection, WebSocketConnectionClosedException


class DyffiBusClient:
    def __init__(self, api_url):
        self.api_url = api_url.rstrip('/')

    def publish(self, topic, payload):
        url = f"{self.api_url}/publish"
        data = json.dumps({"topic": topic, "payload": payload})
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
        c.setopt(c.POSTFIELDS, data)
        c.setopt(c.WRITEDATA, buffer)
        try:
            c.perform()
        finally:
            c.close()
        response_body = buffer.getvalue().decode('utf-8')
        response_json = json.loads(response_body)
        return response_json.get("message_id")

    def publish_async(self, topic, payload, callback=None):
        url = f"{self.api_url}/publish"
        data = json.dumps({"topic": topic, "payload": payload})
        thread = threading.Thread(target=self._publish_thread, args=(url, data, callback), daemon=True)
        thread.start()

    def _publish_thread(self, url, data, callback):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
        c.setopt(c.POSTFIELDS, data)
        c.setopt(c.WRITEDATA, buffer)
        try:
            c.perform()
            response_body = buffer.getvalue().decode('utf-8')
            response_json = json.loads(response_body)
            result = response_json.get("message_id")
            if callback:
                callback(result)
        except Exception as e:
            print("Error in async publish:", e)
            if callback:
                callback(None)
        finally:
            c.close()

    def subscribe(self, topic, handler, blocking=False):
        if blocking:
            self._subscribe_thread(topic, handler)
        else:
            thread = threading.Thread(target=self._subscribe_thread, args=(topic, handler), daemon=True)
            thread.start()

    def _subscribe_thread(self, topic, handler):
        ws_url = self.api_url.replace("http", "ws") + f"/ws/{topic}"
        try:
            ws = create_connection(ws_url)
            while True:
                message_json = ws.recv()
                message = json.loads(message_json)
                handler(message)
        except WebSocketConnectionClosedException:
            print("WebSocket connection closed.")
        except Exception as e:
            print(f"Error: {e}")

    def listen(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
