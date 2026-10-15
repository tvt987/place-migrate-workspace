using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http.Json;
using System.Text.Json;
using Coc.Web.Place.ObjectCore.PLA;

class Program
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
            PropertyNamingPolicy = null, // PascalCase
            PropertyNameCaseInsensitive = true
        };

        // Test with object type:
        object obj = req;
        var content = JsonContent.Create(obj, obj.GetType(), options: options);
        var ms = new MemoryStream();
        content.CopyToAsync(ms).Wait();
        ms.Position = 0;
        string json = new StreamReader(ms).ReadToEnd();

        Console.WriteLine("STJ with PropertyNamingPolicy = null:");
        Console.WriteLine(json);
    }
}
