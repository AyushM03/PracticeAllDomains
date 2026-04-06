// See https://aka.ms/new-console-template for more information

// this will generate the images just put the api key and run dotnet run in terminal.
using  OpenAI_API;

var api = new OpenAIAPI("OPENAPIKEY");

var request= new OpenAI_API.Images.ImageGenerationRequest
{
    Prompt = "a white siamese cat",
};

var response = await api.ImageGenerations.CreateImageAsync(request);
Console.WriteLine("Image URL: {0}",response.Data[0].Url);