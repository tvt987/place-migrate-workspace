using System;
using System.Collections.Generic;
using System.Linq;
using CoC.Web.Place.ViewModels.ShareViewModels;
using System.Net.Http;
using Core.MVC;
using Core.Cache;
using Core.Log.Interface;
using Core.Log;
using System.Net.Http.Headers;
using Core.DTO.Response;
using Core.Infrastructure;
//AI[MIGRATE_START]: System.Web (HttpContext.Current), System.Web.Hosting (QueueBackgroundWorkItem), System.Web.Script.Serialization and WebApiContrib.Formatting.ProtoBuf have no net10.0 surface: request context via IHttpContextAccessor, session user via UserSessionStore, background cache warm via Task.Run, JSON via JsonConvert, protobuf via protobuf-net; SetBearerToken is the IdentityModel HttpClient extension. The synchronous IApiHelper surface is kept for the 60+ CommonHelper call sites (migration-decisions D1, SYNC-DEBT-001)
using System.Threading.Tasks;
using IdentityModel.Client;
using Microsoft.AspNetCore.Http;
using Newtonsoft.Json;
//AI[MIGRATE_END]

namespace CoC.Web.Place.Helpers
{
    public class ApiHelper : IApiHelper
    {
        private UserPrincipal CurrentUser;
        private IAPIClient _ObjAPIClient;

        private string _mediaType = HeaderMediaType.json;

        //private ICacheHelper _CacheHelper;
        private ICacheManager _CacheManager;

        //private IAPIClient _ObjAPIClientWithEtag;
        //private IAPIClient _ObjAPIClientWithoutEtag;

        private ILogger _logger;

        private string _CacheKeyDelete;

        private CodeStep _CodeStep = new CodeStep();
        //private HttpClientType _requestCache = HttpClientType.RequestWithEtag;
        private LogIdentify _logIdentify { get; set; }

        //AI[MIGRATE_START]: HttpContext.Current is static System.Web state (null on Core) so the request context arrives through DI (Startup AddHttpContextAccessor, visible to Autofac via the factory)
        private readonly IHttpContextAccessor _httpContextAccessor;
        //AI[MIGRATE_END]
        //public HttpClientType SetClientType { set { this._requestCache = value; } }
        public CodeStep objCodeStep { get { return _CodeStep; } set { this._CodeStep = value; } }
        public string CacheKeyDelete { set { _CacheKeyDelete = value; } }
        public string MediaType { set { _mediaType = value; } }

        //AI[MIGRATE_START]: ctor gains IHttpContextAccessor (replaces HttpContext.Current); ICacheManager stays keyed "memorycache" by the registrar
        public ApiHelper(IAPIClient objAPIClient, ILogger logger, ICacheManager cacheManager, IHttpContextAccessor httpContextAccessor)
        {
            _ObjAPIClient = objAPIClient;
            _logger = logger;
            _CacheManager = cacheManager;
            _httpContextAccessor = httpContextAccessor;
        }
        //AI[MIGRATE_END]

        public bool RemoveCache(string CacheKey)
        {
            _CacheManager.RemoveByPattern(CacheKey);
            Dictionary<string, object> param = new Dictionary<string, object>();
            param.Add("CacheKey", CacheKey);
            //return GetMethod<bool>(ApiEndPoint.UtilitieResource + "RemoveCache", param);
            return true;
        }

        public void GetResource()
        {
            //AI[MIGRATE_START]: HttpContext.Current.Session["UserPricinpal"] live object -> UserSessionStore (principal + tokens overlay so the Bearer token is present)
            var httpContext = _httpContextAccessor.HttpContext;
            if (this.CurrentUser == null && httpContext != null && UserSessionStore.HasUser(httpContext.Session))
                this.CurrentUser = UserSessionStore.Load(httpContext.Session);
            //AI[MIGRATE_END]

            _logIdentify = new LogIdentify()
            {
                ProcessID = Guid.NewGuid().ToString()
            };

            _CodeStep.ErrorStep = "Set token";
            _ObjAPIClient.Client.SetBearerToken(CurrentUser.Token);
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("UserID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("UserID", CurrentUser.Username);
            //AI[MIGRATE_START]: HttpContext.Current.Items / Session.SessionID -> accessor HttpContext.Items / ISession.Id (same header names and values)
            if (httpContext.Items.ContainsKey("ConcungContextID") && !_ObjAPIClient.Client.DefaultRequestHeaders.Contains("ConcungContextID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("ConcungContextID", httpContext.Items["ConcungContextID"].ToString());
            if (!_ObjAPIClient.Client.DefaultRequestHeaders.Contains("SessionID"))
                _ObjAPIClient.Client.DefaultRequestHeaders.Add("SessionID", httpContext.Session.Id);
            //AI[MIGRATE_END]

            _ObjAPIClient.Client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(_mediaType));
        }

        public T ReadAll<T>(string ApiEndPoint, string CacheKey, Dictionary<string, object> param = null, bool IsReadOnlyCache = false) where T : new()
        {
            this.GetResource();

            T Result = new T();
            if (!string.IsNullOrEmpty(CacheKey) && IsReadOnlyCache)
            {
                if (!_CacheManager.IsSet(CacheKey))
                {
                    this.ReadCacheBacground<T>(ApiEndPoint, CacheKey, param);
                }
                else
                {
                    Result = _CacheManager.Get<T>(CacheKey, () =>
                    {
                        return Result;
                    });
                }
                return Result;
            }

            if (this._CacheManager == null || string.IsNullOrEmpty(CacheKey))
            {
                _CodeStep.ErrorStep = "Call API";
                using (var response = _ObjAPIClient.Get(ApiEndPoint, param))
                {
                    _CodeStep.ErrorStep = "Handling API Respone";
                    SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, param);
                    //T objResponse = response.Content.ReadAsAsync<T>(new[] { new ProtoBufFormatter() }).Result;
                    T objResponse = getContent<T>(response.Content);
                    _CodeStep.Status = JsonStatusViewModels.Success;
                    return objResponse;
                }
            }
            else
            {

                Result = _CacheManager.Get<T>(CacheKey, () =>
                {
                    _CodeStep.ErrorStep = "Call API";
                    using (var response = _ObjAPIClient.Get(ApiEndPoint, param))
                    {
                        _CodeStep.ErrorStep = "Handling API Respone";
                        SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, param);
                        T objResponse = getContent<T>(response.Content);
                        _CodeStep.Status = JsonStatusViewModels.Success;
                        return objResponse;
                    }
                });
            }
            return Result;
        }

        public T1 ReadAllWithPost<T1>(string ApiEndPoint, string CacheKey, object objPara) where T1 : new()
        {
            this.GetResource();

            T1 Result = new T1();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.PostObject(ApiEndPoint, objPara))
            {
                _CodeStep.ErrorStep = "Handling API Respone";
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, objPara);
                //T1 objResponse = response.Content.ReadAsAsync<T1>(new[] { new ProtoBufFormatter() }).Result;
                T1 objResponse = getContent<T1>(response.Content);
                _CodeStep.Status = JsonStatusViewModels.Success;
                return objResponse;
            }
        }

        public void ReadCacheBacground<T>(string ApiEndPoint, string CacheKey, Dictionary<string, object> param = null)
        {
            this.GetResource();
            //AI[MIGRATE_START]: HostingEnvironment.QueueBackgroundWorkItem is System.Web-only -> Task.Run with the same best-effort cache-warm semantics (OLD work was non-critical: a miss just returns the empty result); HttpContext is not available on the pool thread so the bearer values are captured on the request thread first
            var bgToken = CurrentUser != null ? CurrentUser.Token : null;
            var bgUsername = CurrentUser != null ? CurrentUser.Username : null;
            Task.Run(() =>
            //AI[MIGRATE_END]
            {
                lock (CacheKeys.LockObject[CacheKey])
                {
                    if (!_CacheManager.IsSet(CacheKey))
                    {
                        CodeStep _CodeStep2 = new CodeStep();
                        try
                        {
                            IAPIClient apiClient = Engine.ContainerManager.Resolve<IAPIClient>();
                            //AI[MIGRATE_START]: CurrentUser.Token/Username captured before Task.Run (request-scoped values)
                            apiClient.Client.SetBearerToken(bgToken);
                            apiClient.Client.DefaultRequestHeaders.Add("UserID", bgUsername);
                            apiClient.Client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(_mediaType));
                            apiClient.Client.SetBearerToken(bgToken);
                            //AI[MIGRATE_END]
                            using (var response = apiClient.Get(ApiEndPoint, param))
                            {
                                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, param);
                                T objResponse = getContent<T>(response.Content);
                                _CodeStep.Status = JsonStatusViewModels.Success;
                                _CacheManager.Set<T>(CacheKey,
                                        objResponse
                                , Core.Cache.Config.DefaultCacheTime);
                            }
                        }
                        catch (Exception objEx)
                        {  
                            _CodeStep2.ErrorStep = "Log ReadCacheBacground: ";
                            _CodeStep2.ErrorMessage = objEx.Message;
                            _CodeStep2.Data = objEx.StackTrace;
                            //AI[MIGRATE_START]: JavaScriptSerializer (System.Web.Extensions) -> JsonConvert (code-quality-gates G1)
                            _logger.Error(_logIdentify, JsonConvert.SerializeObject(_CodeStep2));
                            //AI[MIGRATE_END]
                        }
                    }
                }
            });
        }

        public T ReadByID<T>(string ApiEndPoint, string Para) where T : new()
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Get(ApiEndPoint + Para))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, Para);
                _CodeStep.ErrorStep = "Read Response";
                T objResponse = getContent<T>(response.Content);
                _CodeStep.Status = JsonStatusViewModels.Success;
                return objResponse;
            }
        }

        /// <summary>
        /// Call Method API Create One
        /// </summary>
        /// <typeparam name="T1">Type Object Request</typeparam>
        /// <typeparam name="T2">Type Response from API</typeparam>
        /// <param name="ApiEndPoint">API Resource</param>
        /// <param name="reqObj">Object Request</param>
        /// <param name="Output">Type Output</param>
        /// <returns>bool</returns>
        public bool Create<T1, T2>(string ApiEndPoint, T1 reqObj, out T2 Output) where T1 : new()
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Post<T1>(ApiEndPoint, reqObj))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, reqObj);
                _CodeStep.ErrorStep = "Read Response";
                CreateRes<T2> objResponse = getContent<CreateRes<T2>>(response.Content);
                Output = objResponse.ID;
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(_CacheKeyDelete))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + _CacheKeyDelete;
                    RemoveCache(_CacheKeyDelete);
                    _CacheKeyDelete = "";
                }
                return true;
            }
        }

        /// <summary>
        /// Call Method API multiple Create
        /// </summary>
        /// <typeparam name="T1">Type Object Request</typeparam>
        /// <typeparam name="T2">Type Response from API</typeparam>
        /// <param name="ApiEndPoint">API Resource</param>
        /// <param name="reqObj">Object Request</param>
        /// <param name="Output">Type Output</param>
        /// <returns>bool</returns>
        public bool Creates<T1, T2>(string ApiEndPoint, T1 reqObj, out List<T2> Output) where T1 : new()
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Post<T1>(ApiEndPoint, reqObj))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, reqObj);
                _CodeStep.ErrorStep = "Read Response";
                //AI[MIGRATE_START]: gold-align - Core.DTO 1.0.5 dropped CreatesRes<> (the plural create response) - UpdatesRes<T2> carries the same IDs:IEnumerable<T> contract, so it stands in for both methods
                UpdatesRes<T2> objResponse = getContent<UpdatesRes<T2>>(response.Content);
                //response.Content.ReadAsAsync<CreatesRes<T2>>(new[] { new ProtoBufFormatter() }).Result;
                Output = objResponse.IDs.ToList();
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(_CacheKeyDelete))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + _CacheKeyDelete;
                    RemoveCache(_CacheKeyDelete);
                    _CacheKeyDelete = "";
                }
                return true;
            }
        }

        /// <summary>
        /// Call Method API Update
        /// </summary>
        /// <typeparam name="T">Type Object Request</typeparam>
        /// <param name="ApiEndPoint">API Resource + ID (/api/id)</param>
        /// <param name="reqObj">Object Request</param>
        /// <returns>Object UpdateRes</returns>
        public bool Update<T>(string ApiEndPoint, T reqObj) where T : new()
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Put<T>(ApiEndPoint, reqObj))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, reqObj);
                _CodeStep.ErrorStep = "Read Response";
                UpdateRes objResponse = getContent<UpdateRes>(response.Content);
                //response.Content.ReadAsAsync<UpdateRes>(new[] { new ProtoBufFormatter() }).Result;
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(_CacheKeyDelete))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + _CacheKeyDelete;
                    RemoveCache(_CacheKeyDelete);
                    _CacheKeyDelete = "";
                }
                return true;
            }
        }

        public bool Updates<T1, T2>(string ApiEndPoint, T1 reqObj, out List<T2> Output) where T1 : new()
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Put<T1>(ApiEndPoint, reqObj))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, reqObj);
                _CodeStep.ErrorStep = "Read Response";
                UpdatesRes<T2> objResponse = getContent<UpdatesRes<T2>>(response.Content);
                //response.Content.ReadAsAsync<UpdatesRes<T2>>(new[] { new ProtoBufFormatter() }).Result;
                Output = objResponse.IDs.ToList();
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(_CacheKeyDelete))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + _CacheKeyDelete;
                    RemoveCache(_CacheKeyDelete);
                    _CacheKeyDelete = "";
                }
                return true;
            }
        }

        /// <summary>
        /// Call Method API Delete
        /// </summary>
        /// <param name="ApiEndPoint">API Resource</param>
        /// <param name="Para">ID</param>
        /// <returns>bool</returns>
        public bool Delete(string ApiEndPoint, string Para)
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Delete(ApiEndPoint + Para))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, Para);
                _CodeStep.ErrorStep = "Read Response";
                //AI[MIGRATE_START]: gold-align - Core.DTO 1.0.5 dropped DeleteRes; the delete response body is never read (success is StatusCode-based) so UpdateRes (StatusCode + ErrorMessage) is the closest shipped shape
                UpdateRes objResponse = getContent<UpdateRes>(response.Content);
                //response.Content.ReadAsAsync<DeleteRes>(new[] { new ProtoBufFormatter() }).Result;
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(_CacheKeyDelete))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + _CacheKeyDelete;
                    RemoveCache(_CacheKeyDelete);
                    _CacheKeyDelete = "";
                }
                return true;
            }
        }

        public T GetMethod<T>(string ApiEndPoint, Dictionary<string, object> objPara = null)
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Get(ApiEndPoint, objPara))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, objPara);
                _CodeStep.ErrorStep = "Read Response";
                T objResponse = getContent<T>(response.Content);
                //response.Content.ReadAsAsync<T>(new[] { new ProtoBufFormatter() }).Result;
                _CodeStep.Status = JsonStatusViewModels.Success;
                return objResponse;
            }
        }

        public T1 PostMethod<T1, T2>(string ApiEndPoint, T2 objPara, string CacheKey = "")
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.PostObject(ApiEndPoint, objPara))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, objPara);
                _CodeStep.ErrorStep = "Read Response";
                T1 objResponse = getContent<T1>(response.Content);
                // response.Content.ReadAsAsync<T1>(new[] { new ProtoBufFormatter() }).Result;
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(CacheKey))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + CacheKey;
                    RemoveCache(CacheKey);
                }
                return objResponse;
            }
        }

        public T1 PutMethod<T1, T2>(string ApiEndPoint, T2 reqObj, string CacheKey = "") where T2 : new()
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Put<T2>(ApiEndPoint, reqObj))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, reqObj);
                _CodeStep.ErrorStep = "Read Response";
                T1 objResponse = getContent<T1>(response.Content);
                //response.Content.ReadAsAsync<T1>(new[] { new ProtoBufFormatter() }).Result;
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(CacheKey))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + CacheKey;
                    RemoveCache(CacheKey);
                }
                return objResponse;
            }
        }

        public T1 DeleteMethod<T1>(string ApiEndPoint, string Para, string CacheKey = "")
        {
            this.GetResource();

            _CodeStep.ErrorStep = "Call API";
            using (var response = _ObjAPIClient.Delete(ApiEndPoint + Para))
            {
                SetErrorAPI(response.Content, (int)response.StatusCode, ApiEndPoint, Para);
                _CodeStep.ErrorStep = "Read Response";
                T1 objResponse = getContent<T1>(response.Content);
                //response.Content.ReadAsAsync<T1>(new[] { new ProtoBufFormatter() }).Result;
                _CodeStep.Status = JsonStatusViewModels.Success;
                if (!string.IsNullOrEmpty(CacheKey))
                {
                    _CodeStep.ErrorStep = "Xóa cache " + CacheKey;
                    RemoveCache(CacheKey);
                }
                return objResponse;
            }
        }

        #region Function

        /// <summary>
        /// Kiểm tra trạng thái mã lỗi trả về khi gọi API
        /// </summary>
        /// <param name="content"></param>
        /// <param name="StatusCode"></param>
        /// <param name="ApiEndPoint"></param>
        private void SetErrorAPI(HttpContent content, int StatusCode, string ApiEndPoint, object reqObj = null)
        {
            if (reqObj != null) _CodeStep.DataSend = reqObj;
            if (AppConfig.Instance.APIDebug) _CodeStep.SuccessStep = ApiEndPoint;
            if (StatusCode == 200 || StatusCode == 201) return;
            _CodeStep.Status = JsonStatusViewModels.Error;
            _CodeStep.HTTPStatusCode = StatusCode;
            _CodeStep.ErrorStep = string.Format("API error {0}: {1} , ApiEndPoint:{2} ", StatusCode, StatusCodeViewModels.Get(StatusCode), ApiEndPoint);
            List<string> LstResponseError = new List<string>();
            switch (StatusCode)
            {
                case 400:
                    //LstResponseError = content.ReadAsAsync<List<string>>(new[] { new ProtoBufFormatter() }).Result;
                    LstResponseError.Add(getContent<string>(content));
                    _CodeStep.Status = JsonStatusViewModels.Error;
                    _CodeStep.ErrorMessage = string.Join("</br>", LstResponseError);
                    _CodeStep.Message = StatusCodeViewModels.Get(StatusCode);
                    break;
                case 406:
                    //LstResponseError = content.ReadAsAsync<List<string>>(new[] { new ProtoBufFormatter() }).Result;
                    LstResponseError.Add(getContent<string>(content));
                    _CodeStep.Status = JsonStatusViewModels.Warning;
                    _CodeStep.Message = string.Join("</br>", LstResponseError);
                    break;
                case 500:
                    //Response.ErrorRes ResponseError = content.ReadAsAsync<Response.ErrorRes>(new[] { new ProtoBufFormatter() }).Result;
                    Response.ErrorRes ResponseError = getContent<Response.ErrorRes>(content);
                    //AI[MIGRATE_START]: playbook 14/06_dead_config_keys_dedup §6.2 - JsonConvert.DeserializeObject<T>("") returns default(T)=null
                    // (never throws); original assumed "no throw means object populated" so an empty 500 body was an NRE here.
                    // Null-guard keeps the original message chain (400/406/500 already fall back to StatusCodeViewModels).
                    _CodeStep.ErrorMessage = ResponseError?.ErrorMessage;
                    //AI[MIGRATE_END]
                    if (string.IsNullOrEmpty(_CodeStep.Message))
                        _CodeStep.Message = StatusCodeViewModels.Get(StatusCode);
                    break;
                case 204:
                    _CodeStep.Message = string.IsNullOrEmpty(_CodeStep.Define204Message) ? _CodeStep.Message : _CodeStep.Define204Message;
                    _CodeStep.Status = JsonStatusViewModels.Warning;
                    this._ObjAPIClient = Engine.ContainerManager.Resolve<IAPIClient>();
                    throw new Exception(_CodeStep.Message);
                //break;
                default:
                    _CodeStep.Message = StatusCodeViewModels.Get(StatusCode);
                    break;
            }
            //AI[MIGRATE_START]: HttpContext.Current.Session.SessionID -> ISession.Id through the accessor
            //AI[MIGRATE_START]: gold-align - NuGet Core.Log 1.0.16 LogIdentify uses SessionID (the vendor DLL key SessIonID was a typo); session id via the accessor
            _logIdentify.SessionID = _httpContextAccessor.HttpContext?.Session?.Id;
            //AI[MIGRATE_END]

            System.Text.StringBuilder srtLog = new System.Text.StringBuilder();
            srtLog.Append("CurrentUser.UserID: ").Append(CurrentUser.UserID).Append("\r\n");
            srtLog.Append("Message: ").Append(_CodeStep.Message).Append("\r\n");
            srtLog.Append("SuccessStep: ").Append(_CodeStep.GetSuccessStep).Append("\r\n");
            srtLog.Append("ErrorStep: ").Append(_CodeStep.GetErrorStep).Append("\r\n");
            srtLog.Append("ErrorMessage: ").Append(_CodeStep.GetErrorMessage).Append("\r\n");
            srtLog.Append("DataSend: ").Append(_CodeStep.GetDataSend);
            srtLog.Append("\r\n");
            srtLog.Append("-----------------------------API Herper-----------------------------------").Append("\r\n");
            if (StatusCode == (int)HTTPStatusCode.ServerError)
                _logger.Error(_logIdentify, srtLog.ToString());
            else
                _logger.Warn(_logIdentify, srtLog.ToString());
            throw new Exception(_CodeStep.Message);
        }

        private T getContent<T>(HttpContent content)
        {
            //AI[MIGRATE_START]: playbook 14 §6.3 - mediaType default json; JSON-first parse via ReadAsStringAsync +
            // JsonConvert (drops the WebApi.Client ReadAsAsync dependency that PagingResponse<T> has no ProtoContract
            // for). protobuf branch kept only for a body that is genuinely binary protobuf; a UTF-8 body that parses as
            // JSON is treated as JSON even under x-protobuf Accept (server ignoring Accept and returning JSON).
            var body = content.ReadAsStringAsync().Result;
            if (!string.IsNullOrEmpty(body))
            {
                try
                {
                    return JsonConvert.DeserializeObject<T>(body);
                }
                catch (JsonException)
                {
                    // fall through to protobuf only if body is not JSON
                }
            }
            switch (_mediaType)
            {
                case "application/x-protobuf":
                    //AI[MIGRATE_START]: WebApiContrib ProtoBufFormatter (net45-only) -> protobuf-net Serializer over the response stream, same wire format and same blocking read as OLD (SYNC-DEBT-001)
                    return ProtoBuf.Serializer.Deserialize<T>(content.ReadAsStreamAsync().Result);
                    //AI[MIGRATE_END]
                case "application/json":
                    return JsonConvert.DeserializeObject<T>(body);
                default:
                    throw new Exception("MediaType Unknow");
            }
        }

        public void LogError(Exception objEx)
        {
            //AI[MIGRATE_START]: HttpContext.Current.Session -> accessor + UserSessionStore; Session.SessionID -> ISession.Id
            var httpContext = _httpContextAccessor.HttpContext;
            if (this.CurrentUser == null && httpContext != null && UserSessionStore.HasUser(httpContext.Session))
                this.CurrentUser = UserSessionStore.Load(httpContext.Session);
            //AI[MIGRATE_END]
            int userID = 0;
            if (this.CurrentUser != null)
            {
                userID = CurrentUser.UserID;
            }
            _logIdentify = new LogIdentify()
            {
                ProcessID = Guid.NewGuid().ToString()
            };
            //AI[MIGRATE_START]: HttpContext.Current.Session.SessionID -> ISession.Id through the accessor
            //AI[MIGRATE_START]: gold-align - NuGet Core.Log 1.0.16 LogIdentify uses SessionID (the vendor DLL key SessIonID was a typo)
            _logIdentify.SessionID = httpContext?.Session?.Id;
            //AI[MIGRATE_END]

            string Message = _CodeStep.Message == null ? "" : _CodeStep.Message;
            string ErrorStep = _CodeStep.GetErrorStep == null ? "" : _CodeStep.GetErrorStep;
            string ErrorMessage = _CodeStep.GetErrorMessage == null ? "" : _CodeStep.GetErrorMessage;
            string objEx_Message = objEx.Message == null ? "" : objEx.Message;

            System.Text.StringBuilder srtLog = new System.Text.StringBuilder();
            srtLog.Append("CurrentUser.UserID: ").Append(userID).Append("\r\n");
            srtLog.Append("Message: ").Append(Message).Append("\r\n");
            srtLog.Append("ErrorStep: ").Append(ErrorStep).Append("\r\n");
            srtLog.Append("ErrorMessage: ").Append(ErrorMessage).Append("\r\n");
            srtLog.Append("DataSend:").Append(_CodeStep.GetDataSend);
            srtLog.Append("\r\n");
            srtLog.Append("objEx.Message: ").Append(objEx.Message).Append("\r\n");
            srtLog.Append("objEx.StackTrace: ").Append(objEx.StackTrace).Append("\r\n");
            srtLog.Append("objEx.InnerException: ").Append(objEx.InnerException).Append("\r\n");
            srtLog.Append("-----------------------------Exception-----------------------------------").Append("\r\n");
            if (_CodeStep.HTTPStatusCode == (int)HTTPStatusCode.ServerError || _CodeStep.HTTPStatusCode == 0)
                _logger.Error(_logIdentify, srtLog.ToString());
            else
                _logger.Warn(_logIdentify, srtLog.ToString());
        }

        #endregion Function
    }
}
