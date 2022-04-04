import pings

p = pings.Ping()
response = p.ping("google.com")
response.is_reached()
response.print_messages()