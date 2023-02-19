wrk.method = "POST"
wrk.body   = "{"Origin": "Dublin", "Destination": "Aberdeen", "Airline": "Emirates", "Terminal": "T1", "Weekday": "Monday", "ScheduledTime": "10"}"
wrk.headers["Content-Type"] = "application/json"