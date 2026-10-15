using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http.Json;
using System.Text.Json;
using Coc.Web.Place.ObjectCore.PLA;
using Newtonsoft.Json;

class CompareJson
{
    static void Main()
    {
        var req = new PlaceSearchMVCReq
        {
            ScopeStatusID = new List<int> { 5, 4, 101 },
            ScopeIDs = new List<int>()
        };

        string newtonsoft = JsonConvert.SerializeObject(req);
        
        // STJ with type object:
        var contentObj = JsonContent.Create((object)req, typeof(object));
        var msObj = new MemoryStream();
        contentObj.CopyToAsync(msObj).Wait();
        msObj.Position = 0;
        string stjObj = new StreamReader(msObj).ReadToEnd();

        // STJ with runtime type:
        var contentReal = JsonContent.Create(req);
        var msReal = new MemoryStream();
        contentReal.CopyToAsync(msReal).Wait();
        msReal.Position = 0;
        string stjReal = new StreamReader(msReal).ReadToEnd();

        Console.WriteLine("Newtonsoft: " + newtonsoft);
        Console.WriteLine("STJ (object): " + stjObj);
        Console.WriteLine("STJ (PlaceSearchMVCReq): " + stjReal);
    }
}
