//AI[MIGRATE_START]: gold-align — IAPIClient/APIClient lived in the OLD vendor DLL.Web/Core.MVC.dll (decompiled to confirm the exact contract: thin HttpClient wrapper, System.Web.Mvc-era codebase, no CCI framework dependency). The NuGet CCI.Core.MVC 1.0.60 replacement package is a redesigned framework (HostBuilderItem/GlobalEngine/PermissionMVC/...) that does not ship this type at all — confirmed by exhaustive decompile of CCI.Core.MVC, CCI.Core.Cache, CCI.Core.Common, CCI.Core.DTO, CCI.Core.Log, CCI.Core.Utilities, CCI.Core.ClientHelper (none define IAPIClient/APIClient). Ported locally, same contract, same behavior (System.Web.HttpUtility.ParseQueryString has no net10 surface so query-string building is done with Uri.EscapeDataString instead; .Result blocking calls become .GetAwaiter().GetResult() to match this codebase's established SYNC-DEBT-001 convention, not a behavior change).
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Json;

namespace CoC.Web.Place.Helpers
{
    public interface IAPIClient : IDisposable
    {
        HttpClient Client { get; }

        HttpResponseMessage Get(string EndPoint, Dictionary<string, object> param = null);

        HttpResponseMessage Post<T>(string EndPoint, T Obj);

        HttpResponseMessage PostObject(string EndPoint, object Obj);

        HttpResponseMessage Put<T>(string EndPoint, T Obj);

        HttpResponseMessage PutObject(string EndPoint, object Obj);

        HttpResponseMessage Delete(string EndPoint);
    }

    public class APIClient : IAPIClient, IDisposable
    {
        protected readonly HttpClient _client;

        protected HttpResponseMessage _response;

        private bool disposedValue = false;

        public HttpClient Client => _client;

        public APIClient(HttpClient client)
        {
            _client = client;
        }

        public virtual HttpResponseMessage Get(string EndPoint, Dictionary<string, object> param = null)
        {
            string queryString = BuildQueryString(param);
            _response = string.IsNullOrWhiteSpace(queryString)
                ? _client.GetAsync(EndPoint).GetAwaiter().GetResult()
                : _client.GetAsync(EndPoint + "?" + queryString).GetAwaiter().GetResult();
            return _response;
        }

        public virtual HttpResponseMessage Post<T>(string EndPoint, T Obj)
        {
            _response = _client.PostAsJsonAsync(EndPoint, Obj).GetAwaiter().GetResult();
            return _response;
        }

        public HttpResponseMessage PostObject(string EndPoint, object Obj)
        {
            _response = _client.PostAsJsonAsync(EndPoint, Obj).GetAwaiter().GetResult();
            return _response;
        }

        public virtual HttpResponseMessage Put<T>(string EndPoint, T Obj)
        {
            _response = _client.PutAsJsonAsync(EndPoint, Obj).GetAwaiter().GetResult();
            return _response;
        }

        public HttpResponseMessage PutObject(string EndPoint, object Obj)
        {
            _response = _client.PutAsJsonAsync(EndPoint, Obj).GetAwaiter().GetResult();
            return _response;
        }

        public virtual HttpResponseMessage Delete(string EndPoint)
        {
            return _client.DeleteAsync(EndPoint).GetAwaiter().GetResult();
        }

        private static string BuildQueryString(Dictionary<string, object> param)
        {
            if (param == null || param.Count == 0) return string.Empty;
            return string.Join("&", param
                .Where(kv => kv.Value != null && !string.IsNullOrWhiteSpace(kv.Value.ToString()))
                .Select(kv => Uri.EscapeDataString(kv.Key) + "=" + Uri.EscapeDataString(kv.Value.ToString())));
        }

        private void Dispose(bool disposing)
        {
            if (disposedValue) return;
            if (disposing)
            {
                _response?.Dispose();
                _client.Dispose();
            }
            disposedValue = true;
        }

        public void Dispose()
        {
            Dispose(disposing: true);
            GC.SuppressFinalize(this);
        }

        ~APIClient()
        {
            Dispose(disposing: false);
        }
    }
}
//AI[MIGRATE_END]
