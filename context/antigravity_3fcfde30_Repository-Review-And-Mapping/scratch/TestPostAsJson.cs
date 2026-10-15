using System;
using System.Net.Http;
using System.Net.Http.Json;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace MyTest
{
    public class PlaceSearchMVCReq
    {
        public List<int> ProvinceID { get; set; }
        public List<int> ScopeTypeRankID { get; set; }
        public List<int> ScopeStatusID { get; set; }
        public int? UserIDFilter { get; set; }
        public List<int> ScopeIDs { get; set; } = new List<int>();
        public bool IsAll { get; set; }
        public bool IsNearStore { get; set; }
        public List<int> ReferSystemIDs { get; set; }
        public List<int> StoreSizeIDs { get; set; }
    }

    class Program
    {
        static async Task Main()
        {
            var client = new HttpClient();
            string token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJCWGoxc3A4NFNmQlM5Xzg2RTItUlVVcjFpN19Wd3pxX2pROUhMZkMyUl9ZIn0.eyJleHAiOjE3OTA2NzgxMDIsImlhdCI6MTc5MDY3NzIwMiwianRpIjoiNGU0Y2U4MTItN2IxMS1iNDZmLTU0ZTAtMzg3MjYxMDZlY2FiIiwiaXNzIjoiaHR0cHM6Ly9pZHMxLXN0Zy5jb25jdW5nLnZuL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJwbGFjZS5jb25jdW5nLmNvbSIsInN1YiI6ImY6YTE4NzA0M2ItNDgxMC00NGUwLWJlNTAtNTQyZDg0ZWQxNzM3OjE3NDIiLCJ0eXAiOiJJRCIsImF6cCI6InBsYWNlLmNvbmN1bmcuY29tIiwibm9uY2UiOiI3MDQyNmYxZjhjZTk0YTdlOTlhMmI1NjFmMWQ1NDkwZSIsInNpZCI6ImRtXzRpOExiYXJHQ2xVM0l0SE9BaWdRRiIsImF0X2hhc2giOiJnM21SX0hLT25EQjZFb0E4X2dtSGtBIiwiZ2VuZGVyIjoiMSIsIi9FbXBsb3llZUlEIjoiMCIsIi9Qb3NpdGlvbklEIjoiMzMyIiwidnBuX3VzZXJuYW1lIjoiIiwiL1N0b3JlSUQiOiI2ODciLCJyb2xlX2lkcyI6IlszMTQ3LCAzMTUzLCAzMTc2LCAzMTc5LCAzMTg1LCAzMTg3LCAzMTk0LCAzMjIxLCAzMjQ4LCAzMjgxLCAzMjgzLCAzMjk4LCAzMzAxLCAzMzA5LCAzMzE0LCAzMzI4LCAzMzMyLCAzMzM4LCAzMzQwLCAzMzQ0LCAzMzQ3LCAzMzkyLCAzNDAxLCAzNDMxLCAzNDkzLCAzNDk1LCAzNTA1LCAzNTA3LCAzNTE1LCAzNTI0LCAzNTQ2LCAzNTU0LCAzNTc5LCAzNTg3LCAzNjQwLCAzNjcyLCAzNzEwLCAzNzIzLCAzNzkzLCAzNzk4LCA0MTIyLCA0MTI1XSIsIi9EZXBhcnRtZW50SUQiOiIzMzAiLCJ1c2VyX3R5cGVfaWQiOiIxIiwic3RvcmVfaWQiOiI2ODciLCIvVXNlcklEIjoiMTc0MiIsIi9Vc2VyVHlwZUlEIjoiMSIsIi9WUE5QYXNzd29yZCI6IiIsIi9GdWxsbmFtZSI6IkzDqiBI4buTIEhp4bq_dSBHaWFuZyIsImRlcGFydG1lbnRfaWQiOiIzMzAiLCIvU3VwcGxpZXJJRCI6IjAiLCJhdmF0YXIiOiJhdmEvMjAxOC8xNV8xMl8yMDE2XzEwXzQ3XzExMTUyNDE4MjdfMTI4MzM0MjMwMTczODM1N182NTEyNzkxNTg5MTMwMTQzOTg5X24uanBnIiwidnBuX3Bhc3N3b3JkIjoiIiwiL1VzZXJuYW1lIjoiMjc0MSIsIi9Sb2xlSURzIjoiWzMxNDcsIDMxNTMsIDMxNzYsIDMxNzksIDMxODUsIDMxODcsIDMxOTQsIDMyMjEsIDMyNDgsIDMyODEsIDMyODMsIDMyOTgsIDMzMDEsIDMzMDksIDMzMTQsIDMzMjgsIDMzMzIsIDMzMzgsIDMzNDAsIDMzNDQsIDMzNDcsIDMzOTIsIDM0MDEsIDM0MzEsIDM0OTMsIDM0OTUsIDM1MDUsIDM1MDcsIDM1MTUsIDM1MjQsIDM1NDYsIDM1NTQsIDM1NzksIDM1ODcsIDM2NDAsIDM2NzIsIDM3MTAsIDM3MjMsIDM3OTMsIDM3OTgsIDQxMjIsIDQxMjVdIiwiL0F2YXRhciI6ImF2YS8yMDE4LzE1XzEyXzIwMTZfMTBfNDdfMTExNTI0MTgyN18xMjgzMzQyMzAxNzM4MzU3XzY1MTI3OTE1ODkxMzAxNDM5ODlfbi5qcGciLCJ1c2VyX2lkIjoiMTc0MiIsImVtcGxveWVlX2lkIjoiMCIsIi9WUE5Vc2VybmFtZSI6IiIsImZ1bGxuYW1lIjoiTMOqIEjhu5MgSGnhur91IEdpYW5nIiwic3VwcGxpZXJfaWQiOiIwIiwidXNlcm5hbWUiOiIyNzQxIiwiL0dlbmRlciI6IjEiLCJwb3NpdGlvbl9pZCI6IjMzMiJ9.dvzYExeO68vS8KznkUEJh5p4uesa-ksAhN663SrLRCpw5gDce1wxEifEVIpkFzjGR7NtyXMiJIgDdjWW_93P-KQ2YNs386Mcb3zLbpd_8rpKEKsujtHl9fpvJMgHVUsOwNRZT1v9VJHEpbldj4ursLFo4HZp1deCRnN76EEeAWCaqhmsGxf0E5jpq27m7uDbSFtyJ1ocNIYdoK6PoV0AyVU0IBHqTnB9L5nJXgpCkl8HajShdGNCXy90CCJf6keNeR5FT7UQpQqgv78_nGjDT7_hpFlHQ-B1cYSkT_sP7wCxrtg1vnsIRi99BuoKaWm8-h5BeWisWMDHuwaaPbSyLw";
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            client.DefaultRequestHeaders.Add("UserID", "2741");
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            client.DefaultRequestHeaders.Add("SessionID", "556dd3f3-413f-8d09-dec9-6bc9bcee88ac");

            var req = new PlaceSearchMVCReq
            {
                ScopeStatusID = new List<int> { 5, 4, 101 }
            };
            object obj = req;
            var response = await client.PostAsJsonAsync("https://place-api-stg4.concung.vn/api/Scopes/GetListMVC", obj);
            Console.WriteLine("StatusCode: " + (int)response.StatusCode + " " + response.StatusCode);
            var body = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Body length: " + body.Length + ", preview: " + (body.Length > 200 ? body.Substring(0, 200) : body));
        }
    }
}
