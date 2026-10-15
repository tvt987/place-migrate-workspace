using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Text.Json;
using Coc.Web.Place.ObjectCore.PLA;

namespace TestApp {
    public class Program {
        public static void Main() {
            var req = new PlaceSearchMVCReq {
                ScopeStatusID = new List<int> { 5, 4, 101 },
                ScopeIDs = new List<int>()
            };
            string nj = JsonConvert.SerializeObject(req);
            string stj = System.Text.Json.JsonSerializer.Serialize(req);
            Console.WriteLine("NJ: " + nj);
            Console.WriteLine("STJ: " + stj);
        }
    }
}