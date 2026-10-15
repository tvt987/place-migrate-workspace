using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Net.Http.Json;
using System.Text.Json;
using Coc.Web.Place.ObjectCore.PLA;
using Newtonsoft.Json;

class Program
{
    static void Main()
    {
        var req = new PlaceSearchMVCReq
        {
            ScopeStatusID = new List<int> { 5, 4, 101 },
            ScopeIDs = new List<int>()
        };

        object obj = req;

        // 1. What APIClient.PostObject currently does:
        var content = JsonContent.Create(obj, typeof(object));
        var ms = new MemoryStream();
        content.CopyToAsync(ms).Wait();
        ms.Position = 0;
        using var reader = new StreamReader(ms);
        string stjAsObject = reader.ReadToEnd();
        Console.WriteLine("APIClient.PostObject currently sends: [" + stjAsObject + "]");

        // 2. What Newtonsoft sends:
        string newtonsoftJson = JsonConvert.SerializeObject(obj);
        Console.WriteLine("Newtonsoft sends: [" + newtonsoftJson + "]");
    }
}
