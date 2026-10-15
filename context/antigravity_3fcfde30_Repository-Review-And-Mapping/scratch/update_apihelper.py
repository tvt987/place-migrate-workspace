import os

file_path = r'e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Helpers\ApiHelper.cs'

with open(file_path, 'rb') as f:
    raw = f.read()

has_bom = raw.startswith(b'\xef\xbb\xbf')
text = raw.decode('utf-8-sig')

target = """        private static string getRawContent(HttpContent content)
        {
            try
            {
                return content == null ? string.Empty : content.ReadAsStringAsync().Result;
            }
            catch (Exception)
            {
                return string.Empty;
            }
        }

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
            List<string> LstResponseError = null;
            switch (StatusCode)
            {
                case 400:
                    LstResponseError = tryGetContent<List<string>>(content) ?? new List<string> { getRawContent(content) };
                    _CodeStep.Status = JsonStatusViewModels.Error;
                    _CodeStep.ErrorMessage = string.Join("</br>", LstResponseError);
                    _CodeStep.Message = StatusCodeViewModels.Get(StatusCode);
                    break;
                case 406:
                    LstResponseError = new List<string> { tryGetContent<string>(content) ?? getRawContent(content) };
                    _CodeStep.Status = JsonStatusViewModels.Warning;
                    _CodeStep.Message = string.Join("</br>", LstResponseError);
                    break;
                case 500:
                    if (content.Headers.ContentType != null
                        && content.Headers.ContentType.MediaType == HeaderMediaType.text_plain)
                    {
                        _CodeStep.ErrorMessage = getRawContent(content);
                    }
                    else
                    {
                        Response.ErrorRes ResponseError = tryGetContent<Response.ErrorRes>(content);
                        _CodeStep.ErrorMessage = ResponseError != null && !string.IsNullOrEmpty(ResponseError.ErrorMessage)
                            ? ResponseError.ErrorMessage
                            : getRawContent(content);
                    }
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
            var logSession = _httpContextAccessor?.HttpContext?.Session;
            if (logSession != null) _logIdentify.SessionID = logSession.Id;

            System.Text.StringBuilder srtLog = new System.Text.StringBuilder();
            if (CurrentUser != null)
            {
                srtLog.Append("CurrentUser.UserID: ").Append(CurrentUser?.UserID).Append("\\r\\n");
            }
            srtLog.Append("Message: ").Append(_CodeStep.Message).Append("\\r\\n");
            srtLog.Append("SuccessStep: ").Append(_CodeStep.GetSuccessStep).Append("\\r\\n");
            srtLog.Append("ErrorStep: ").Append(_CodeStep.GetErrorStep).Append("\\r\\n");
            srtLog.Append("ErrorMessage: ").Append(_CodeStep.GetErrorMessage).Append("\\r\\n");
            srtLog.Append("DataSend: ").Append(_CodeStep.GetDataSend);
            srtLog.Append("\\r\\n");
            srtLog.Append("-----------------------------API Herper-----------------------------------").Append("\\r\\n");
            if (StatusCode == (int)HTTPStatusCode.ServerError)
                _logger.Error(_logIdentify, srtLog.ToString());
            else
                _logger.Warn(_logIdentify, srtLog.ToString());
            throw new Exception(_CodeStep.Message);
        }"""

replacement = """        private static string getRawContent(HttpContent content)
        {
            try
            {
                if (content == null) return string.Empty;
                try
                {
                    content.LoadIntoBufferAsync().GetAwaiter().GetResult();
                }
                catch { }
                return content.ReadAsStringAsync().GetAwaiter().GetResult();
            }
            catch (Exception ex)
            {
                return $"[Error reading raw content: {ex.Message}]";
            }
        }

        private static readonly object _localLogLock = new object();

        public static void WriteLocalDebugLog(string logContent)
        {
            try
            {
                var timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff");
                var sb = new System.Text.StringBuilder();
                sb.AppendLine($"========== [{timestamp}] SCM API DEBUG LOG ==========");
                sb.AppendLine(logContent);
                sb.AppendLine("================================================================================");
                sb.AppendLine();

                var entry = sb.ToString();

                System.Diagnostics.Debug.WriteLine(entry);
                Console.WriteLine(entry);

                var logPaths = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

                try
                {
                    var baseDir = AppContext.BaseDirectory;
                    if (!string.IsNullOrEmpty(baseDir))
                        logPaths.Add(System.IO.Path.Combine(baseDir, "api_debug.log"));
                }
                catch { }

                try
                {
                    var curDir = System.IO.Directory.GetCurrentDirectory();
                    if (!string.IsNullOrEmpty(curDir))
                        logPaths.Add(System.IO.Path.Combine(curDir, "api_debug.log"));
                }
                catch { }

                lock (_localLogLock)
                {
                    foreach (var logPath in logPaths)
                    {
                        try
                        {
                            System.IO.File.AppendAllText(logPath, entry, System.Text.Encoding.UTF8);
                        }
                        catch { }
                    }
                }
            }
            catch { }
        }

        /// <summary>
        /// Kiểm tra trạng thái mã lỗi trả về khi gọi API
        /// </summary>
        /// <param name="content"></param>
        /// <param name="StatusCode"></param>
        /// <param name="ApiEndPoint"></param>
        private void SetErrorAPI(HttpContent content, int StatusCode, string ApiEndPoint, object reqObj = null)
        {
            if (content != null)
            {
                try { content.LoadIntoBufferAsync().GetAwaiter().GetResult(); } catch { }
            }
            if (reqObj != null) _CodeStep.DataSend = reqObj;
            if (AppConfig.Instance.APIDebug) _CodeStep.SuccessStep = ApiEndPoint;
            if (StatusCode == 200 || StatusCode == 201) return;
            _CodeStep.Status = JsonStatusViewModels.Error;
            _CodeStep.HTTPStatusCode = StatusCode;
            _CodeStep.ErrorStep = string.Format("API error {0}: {1} , ApiEndPoint:{2} ", StatusCode, StatusCodeViewModels.Get(StatusCode), ApiEndPoint);
            List<string> LstResponseError = null;
            string rawContent = getRawContent(content);
            switch (StatusCode)
            {
                case 400:
                    LstResponseError = tryGetContent<List<string>>(content) ?? new List<string> { rawContent };
                    _CodeStep.Status = JsonStatusViewModels.Error;
                    _CodeStep.ErrorMessage = string.Join("</br>", LstResponseError);
                    _CodeStep.Message = StatusCodeViewModels.Get(StatusCode);
                    break;
                case 406:
                    LstResponseError = new List<string> { tryGetContent<string>(content) ?? rawContent };
                    _CodeStep.Status = JsonStatusViewModels.Warning;
                    _CodeStep.Message = string.Join("</br>", LstResponseError);
                    break;
                case 500:
                    if (content != null && content.Headers.ContentType != null
                        && content.Headers.ContentType.MediaType == HeaderMediaType.text_plain)
                    {
                        _CodeStep.ErrorMessage = rawContent;
                    }
                    else
                    {
                        Response.ErrorRes ResponseError = tryGetContent<Response.ErrorRes>(content);
                        _CodeStep.ErrorMessage = ResponseError != null && !string.IsNullOrEmpty(ResponseError.ErrorMessage)
                            ? ResponseError.ErrorMessage
                            : rawContent;
                    }
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
            var logSession = _httpContextAccessor?.HttpContext?.Session;
            if (logSession != null) _logIdentify.SessionID = logSession.Id;

            System.Text.StringBuilder srtLog = new System.Text.StringBuilder();
            srtLog.Append("Type: [API ERROR]\\r\\n");
            srtLog.Append("ApiEndPoint: ").Append(ApiEndPoint).Append("\\r\\n");
            srtLog.Append("HTTPStatusCode: ").Append(StatusCode).Append(" (").Append(StatusCodeViewModels.Get(StatusCode)).Append(")\\r\\n");
            if (CurrentUser != null)
            {
                srtLog.Append("CurrentUser.UserID: ").Append(CurrentUser?.UserID).Append("\\r\\n");
                srtLog.Append("CurrentUser.Username: ").Append(CurrentUser?.Username).Append("\\r\\n");
                var tokenPreview = string.IsNullOrEmpty(CurrentUser?.Token) ? "(null/empty)" : (CurrentUser.Token.Length > 30 ? CurrentUser.Token.Substring(0, 30) + "..." : CurrentUser.Token);
                srtLog.Append("Token: ").Append(tokenPreview).Append("\\r\\n");
            }
            srtLog.Append("Message: ").Append(_CodeStep.Message).Append("\\r\\n");
            srtLog.Append("SuccessStep: ").Append(_CodeStep.GetSuccessStep).Append("\\r\\n");
            srtLog.Append("ErrorStep: ").Append(_CodeStep.GetErrorStep).Append("\\r\\n");
            srtLog.Append("ErrorMessage: ").Append(_CodeStep.GetErrorMessage).Append("\\r\\n");
            srtLog.Append("DataSend: ").Append(_CodeStep.GetDataSend).Append("\\r\\n");
            srtLog.Append("RawResponseBody: ").Append(rawContent).Append("\\r\\n");
            srtLog.Append("-----------------------------API Herper-----------------------------------\\r\\n");

            WriteLocalDebugLog(srtLog.ToString());

            if (StatusCode == (int)HTTPStatusCode.ServerError)
                _logger.Error(_logIdentify, srtLog.ToString());
            else
                _logger.Warn(_logIdentify, srtLog.ToString());
            throw new Exception(_CodeStep.Message);
        }"""

target_norm = target.replace('\r\n', '\n')
text_norm = text.replace('\r\n', '\n')
repl_norm = replacement.replace('\r\n', '\n')

if target_norm in text_norm:
    new_text = text_norm.replace(target_norm, repl_norm, 1)
    old_log_err = """            srtLog.Append("objEx.InnerException: ").Append(objEx.InnerException).Append("\\r\\n");
            srtLog.Append("-----------------------------Exception-----------------------------------").Append("\\r\\n");
            if (_CodeStep.HTTPStatusCode == (int)HTTPStatusCode.ServerError || _CodeStep.HTTPStatusCode == 0)"""
    new_log_err = """            srtLog.Append("objEx.InnerException: ").Append(objEx.InnerException).Append("\\r\\n");
            srtLog.Append("-----------------------------Exception-----------------------------------\\r\\n");

            WriteLocalDebugLog(srtLog.ToString());

            if (_CodeStep.HTTPStatusCode == (int)HTTPStatusCode.ServerError || _CodeStep.HTTPStatusCode == 0)"""
    old_log_err_norm = old_log_err.replace('\r\n', '\n')
    new_log_err_norm = new_log_err.replace('\r\n', '\n')
    if old_log_err_norm in new_text:
        new_text = new_text.replace(old_log_err_norm, new_log_err_norm, 1)
        print('Replacing LogError succeeded')
    else:
        print('LogError target not found')

    with open(file_path, 'wb') as f:
        if has_bom:
            f.write(b'\xef\xbb\xbf')
        f.write(new_text.encode('utf-8'))
    print('Replacement succeeded, BOM preserved:', has_bom)
else:
    print('Target not found in text!')
