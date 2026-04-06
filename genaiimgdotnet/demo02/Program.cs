using OpenAI_API;
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
// to run program install open ai
// run it on terminal: dotnet add package OpenAI

var key = new APIAuthentication("sk-***********************");

var api =new OpenAIPredictionAPI(key);
var prompt = "What is the capital of France?";
var request = new OpenAI_API.Completions.CompleteRequest(prompt,model: OpenAI_API.Models..Model.DavinciText, temperature: 0.7, max_tokens: 100);
var response = await api.Completions.CreateCompletionAsync(request);
var completion = response.completions[0].text;
Console.WriteLine("GENERATED TEXT: {0}", completion);