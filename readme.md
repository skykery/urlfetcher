# URLFetcher
A microservice that can handle HTTP requests and can serve parsed elements using CSS Selectors and XPath.
The microservice is running on FastAPI as web framework, relies on LXML for the HTML parsing part and is successfully using Tor nodes and proxies to hide the initial request.

To run it locally
`docker-compose -f stack.yaml up -d`

I published a project [URLWorker](https://urlworker.techwetrust.com/) which is based on this microservice and you can try it yourself, for free of course.
![URLWorker](https://i.imgur.com/jcXKTex.png)

You can make a free account on [https://urlworker.techwetrust.com/](https://urlworker.techwetrust.com/) or watch my tutorials on how to use it right on the [Examples](https://urlworker.techwetrust.com/examples/) section.

Don't forget to star the repo for further updates.
