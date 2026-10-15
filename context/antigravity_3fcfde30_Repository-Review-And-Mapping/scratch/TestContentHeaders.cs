using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Json;
using System.Text;
using System.Text.Json;
using Coc.Web.Place.ObjectCore.PLA;

class TestContent
{
    static void Main()
    {
        var req = new PlaceSearchMVCReq
        {
            ScopeStatusID = new List<int> { 5, 4, 101 },
            ScopeIDs = new List<int>()
        };

        var options = new JsonSerializerOptions
        {
            PropertyNamingPolicy = null,
            PropertyNameCaseInsensitive = true
        };

        var json = Newtonsoft.Json.JsonConvert.SerializeObject(req);
        var stringContent = new StringContent(json, Encoding.UTF8, "application/json");

        var jsonContent = JsonContent.Create(req, req.GetType(), options: options);

        Console.WriteLine("=== StringContent Headers ===");
        foreach (var h in stringContent.Headers)
        {
            Console.WriteLine($"{h.Key}: {string.Join(", ", h.Value)}");
        }

        Console.WriteLine("\n=== JsonContent Headers ===");
        foreach (var h in jsonContent.Headers)
        {
            Console.WriteLine($"{h.Key}: {string.Join(", ", h.Value)}");
        }
    }
}
