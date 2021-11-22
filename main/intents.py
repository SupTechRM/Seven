import wolframalpha

app_id = '74XVJK-XLRGUXJH9X'

# Create a client
client = wolframalpha.Client(app_id)

# Get results
res = client.query("What is the capital of France?")

# Get the first pod
pod = next(res.results).text

# print the pod
print(pod)
