import queue
import time
import uuid


request_queue = queue.Queue()


def generate_request():
    request_id = str(uuid.uuid4())
    request_data = {"request_id": request_id, "content": f"Request {request_id}"}
    request_queue.put(request_data)
    print(f"Generated request: {request_data}")


def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Processing request: {request_data}")
    else:
        print("Queue is empty. No requests to process.")


try:
    while True:
        generate_request()
        process_request()
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user.")
