<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    @vite('resources/css/app.css')
</head>
<body class="bg-gray-900">
<div class="container mx-auto py-10 h-full">
    <div class="w-full bg-blue-950 shadow-lg rounded-lg overflow-hidden">
        <div class="px-6 py-4">
            <h1 class="text-3xl font-bold mb-4 text-white text-center uppercase">NLP Chatbot</h1>
            <div id="chat" class="h-64 bg-gray-200 p-4 rounded-lg overflow-y-auto">

            </div>
            <div class="mt-4">
                <input id="message" type="text" class="w-full px-4 py-2 border rounded-lg"
                       placeholder="Type your message...">
            </div>
            <div class="mt-2 text-right">
                <button id="send" class="bg-blue-500 text-white px-4 py-2 rounded-lg capitalize">Ask?</button>
            </div>
        </div>
    </div>
</div>
</body>
</html>
