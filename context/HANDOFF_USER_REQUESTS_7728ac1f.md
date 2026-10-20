# Yêu cầu của user — conversation `Current Progress Check` (7728ac1f)

> 42 yêu cầu, theo thứ tự thời gian (giờ VN). Trích từ `transcript_full.jsonl`.

---

## 1. 18/10/2026 18:03

<USER_REQUEST>
@[e:\Work\Place_Migrate\context\HANDOFF_PROMPT_3fcfde30_20261018.md] và cho tôi biết tiến độ hiện tại
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T18:03:45+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\context\HANDOFF_PROMPT_3fcfde30_20261018.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- e:\Work\Place_Migrate\context\HANDOFF_PROMPT_3fcfde30_20261018.md (LANGUAGE_MARKDOWN)
- e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)

The user has mentioned some items in the form @[ITEM]. Here is extra information about the items that were mentioned by the user, in the order that they appear:

@[e:\Work\Place_Migrate\context\HANDOFF_PROMPT_3fcfde30_20261018.md] is a [File]:
e:\Work\Place_Migrate\context\HANDOFF_PROMPT_3fcfde30_20261018.md
</ADDITIONAL_METADATA>
<USER_SETTINGS_CHANGE>
The user changed setting `Model Selection` from None to Gemini 3.8 Flash (High). No need to comment on this change if the user doesn't ask about it. If reporting what model you are, please use a human readable name instead of the exact string.
</USER_SETTINGS_CHANGE>

---

## 2. 18/10/2026 18:18

<USER_REQUEST>
Lập 1 rule global xuyên xuốt workspace này
1. Chỉ làm việc và sửa code fix code trên @[e:\Work\Place_Migrate\cci-store-location-web] , @[e:\Work\Place_Migrate\cci-dc-web] , @[e:\Work\Place_Migrate\cci-scm-web] và @[e:\Work\Place_Migrate\cci-oneteam-web] nhưng tạm thời peding phần cci-oneteam-web do team migrate chưa triển khai xong, còn lại các project khác trong workpace là để có thêm context để test cũng như là build test cho các project liệt kê trên vì thế không được phép sửa
2. Luôn luôn bám sát phần rule @[e:\Work\Place_Migrate\cci-dc-web\DEV_HANDBOOK.md] @[e:\Work\Place_Migrate\cci-dc-web\FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md] và trong đây có đề cập đến sau khi code đẩy lên nhánh dev thì tiếp tục với nhánh staging và staging10, lưu ý ở đây là ở 2 nhánh staging và staging10 chỉ tạo pull request vì đã có hệ thống trigger auto merge và build, nên buộc phải tạo PR chứ không thực hiện merge và đẩy code một cách thủ công lên 2 nhánh này
3. Mỗi khi thực hiện xong nhiệm vụ phải nhớ lại context bên trong handbook để tránh làm sai
4. https://report-web-testing-uat.concung.vn => dashboard report test của web cho leader xem, leader kêu "mọi người pull code mới về check 03_qa/.env để có credential push report lên theo lệnh make test-* là run xong test case nó tự push report lên dashboard tổng hợp" -> hiện tại thì phần này cần check lại cho dc-web thì leader báo chưa thấy report cho phần test của dc-web, hay là do web report có vấn đề, xem là kết quả report đã được đẩy thành công chưa, trên report hiện tại thấy được có 3 test case trên report của dc-web trên https://report-web-testing-uat.concung.vn coi thử vấn đề là do test hay do phần portal report hoạt động sai, hình như DB của nó ở trong phần cấu hình này 
@[e:\Work\Place_Migrate\cci-dc-web\03_qa\.env] 
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T18:18:49+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\cci-dc-web\03_qa\.env (LANGUAGE_UNSPECIFIED)
Cursor is on line: 40
Other open documents:
- e:\Work\Place_Migrate\cci-dc-web\03_qa\.env (LANGUAGE_UNSPECIFIED)
- e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)

The user has mentioned some items in the form @[ITEM]. Here is extra information about the items that were mentioned by the user, in the order that they appear:

@[e:\Work\Place_Migrate\cci-store-location-web] is a [File]:
e:\Work\Place_Migrate\cci-store-location-web
@[e:\Work\Place_Migrate\cci-dc-web] is a [File]:
e:\Work\Place_Migrate\cci-dc-web
@[e:\Work\Place_Migrate\cci-scm-web] is a [File]:
e:\Work\Place_Migrate\cci-scm-web
@[e:\Work\Place_Migrate\cci-oneteam-web] is a [File]:
e:\Work\Place_Migrate\cci-oneteam-web
@[e:\Work\Place_Migrate\cci-dc-web\DEV_HANDBOOK.md] is a [File]:
e:\Work\Place_Migrate\cci-dc-web\DEV_HANDBOOK.md
@[e:\Work\Place_Migrate\cci-dc-web\FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md] is a [File]:
e:\Work\Place_Migrate\cci-dc-web\FULL_MIGRATION_QA_HANDBOOK_CONTEXT.md
@[e:\Work\Place_Migrate\cci-dc-web\03_qa\.env] is a [File]:
e:\Work\Place_Migrate\cci-dc-web\03_qa\.env
</ADDITIONAL_METADATA>

---

## 3. 18/10/2026 18:32

<USER_REQUEST>
tôi thấy lệnh bạn đưa là test ở net4 còn phần net10 thì cũng phải test luôn, bạn giúp tôi chạy lệnh trên và push report lên dc web
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T18:32:28+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-dc-web\03_qa\.env (LANGUAGE_UNSPECIFIED)
</ADDITIONAL_METADATA>

---

## 4. 18/10/2026 18:53

<USER_REQUEST>
chúng ta cũng sẽ lập 1 global rule để luôn cập nhật kết quả report của từng portal mà chúng ta test vào để kiểm soát và quản lý, và mỗi lần chạy test xong phải so sánh bà báo đó có phải là lỗi migrate không
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T18:53:20+07:00.

The user's current state is as follows:
Active Document: e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)
Cursor is on line: 21
Other open documents:
- e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)
</ADDITIONAL_METADATA>

---

## 5. 18/10/2026 18:56

<USER_REQUEST>
tiếp theo là kiểm tra phần @[e:\Work\Place_Migrate\cci-store-location-web] tương tự như dc bên trên
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T18:56:04+07:00.

The user's current state is as follows:
Active Document: e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)
Cursor is on line: 21
Other open documents:
- e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)

The user has mentioned some items in the form @[ITEM]. Here is extra information about the items that were mentioned by the user, in the order that they appear:

@[e:\Work\Place_Migrate\cci-store-location-web] is a [File]:
e:\Work\Place_Migrate\cci-store-location-web
</ADDITIONAL_METADATA>

---

## 6. 18/10/2026 19:16

<USER_REQUEST>
ngoài việc up lên report, kết quả test, kết quả so sánh nói chung là tiến độ chúng ta nên có 1 file global trong workspace này để ghi lại, và chúng ta sẽ không bị quên hoặc cần truy xuất nhanh, mỗi lần làm gì đấy thì cập nhật tiến độ vào file mới nhất, không cần phải là lưu từng ngày từng version, chỉ cần luôn luôn update mới nhất vào là được
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:16:23+07:00.

The user's current state is as follows:
Active Document: e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)
Cursor is on line: 21
Other open documents:
- e:\Work\dev-ops\vaults-gitops\stg\cci\dc\dc-api-mssql\configs\appsettings.json (LANGUAGE_JSON)
</ADDITIONAL_METADATA>

---

## 7. 18/10/2026 19:22

<USER_REQUEST>
bổ sung rule global là mỗi lần fix một bug gì đó 1 trong các portal web mà mình đang thao tác thì cũng phải quét all các portal web mình thao tác còn lại để fix chung nếu cùng chung vấn đề, và theo handbook thì có vẻ là phải tạo nhánh rồi mới merge vào nhánh dev không biết là đúng không, phần này đã có trong rule global chưa nếu chưa thì thêm vào để tránh sai sót. Trước tiên là fix bug của phần cci-store-location-web mà bạn đã phát hiện bug bên trên\
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:22:18+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 8. 18/10/2026 19:37

<USER_REQUEST>
file nào để chúng ta quan sát tiến độ quá trình vậy
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:37:24+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\cci-store-location-web\04_critical_change\TC-FUNC-005-fallback-idsurl-auth-stg10.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- e:\Work\Place_Migrate\cci-store-location-web\04_critical_change\TC-FUNC-005-fallback-idsurl-auth-stg10.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\03_qa\fixtures\auth.fixture.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 9. 18/10/2026 19:38

<USER_REQUEST>
thêm vào bộ rule tuyệt đối không push các phần message text "Co-Authored-By" này lên trông rất thiếu chuyên nghiệp
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:38:29+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\cci-store-location-web\04_critical_change\TC-FUNC-005-fallback-idsurl-auth-stg10.md (LANGUAGE_MARKDOWN)
Cursor is on line: 1
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\04_critical_change\TC-FUNC-005-fallback-idsurl-auth-stg10.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\03_qa\fixtures\auth.fixture.ts (LANGUAGE_TYPESCRIPT)
</ADDITIONAL_METADATA>

---

## 10. 18/10/2026 19:40

<USER_REQUEST>
phần cci-store-location-web chạy test migrate xong hết chưa, vì tôi thấy trạng thái @[e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md] chỉ để là " ĐÃ FIX BUG AUTH STG10"
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:40:53+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\GIT_RULES.md (LANGUAGE_MARKDOWN)

The user has mentioned some items in the form @[ITEM]. Here is extra information about the items that were mentioned by the user, in the order that they appear:

@[e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md] is a [File]:
e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md
</ADDITIONAL_METADATA>

---

## 11. 18/10/2026 19:46

<USER_REQUEST>
tôi có thể prompt phiên làm việc này với 2 khung chat với 2 sub agents chạy song song không vì đợi prompt xong rồi lại đợi thì lâu quá
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:46:33+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\GIT_RULES.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 12. 18/10/2026 19:49

<USER_REQUEST>
chạy ngầm thành một Background Task test cho toàn bộ scm trong lúc đợi cci-store-location-web deploy thành công tôi sẽ báo lại để chạy cci-store-location-web sau, lưu ý là khi chạy mà gặp lỗi migrate thì dừng test rồi report luôn nha, không phải treo test hết rồi mới trả ra vì scm rất lớn, mà cũng không phải chỉ mỗi scm, tất cả portal mà tôi đang làm việc đều áp dụng nguyên tắc này
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:49:37+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\GIT_RULES.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 13. 18/10/2026 19:57

<USER_REQUEST>
Tôi thấy lúc scm đang run dưới background task thì lúc prompt antigravity đưa prompt chat vào hàng chờ và show message "sends after agent finishes working" vậy nếu tôi click Button "Send now" thì scm có bị dừng không. cci-store-location-web đã deploy done, chạy test luôn cho nó
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T19:57:29+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\GIT_RULES.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 14. 18/10/2026 21:25

<USER_REQUEST>
cci-store-location-web: backend-api-broken (Nguyên nhân gốc của 131 ca fail chênh lệch trên NET10) Chọn Phương án 2 (Vault Config): Sửa dòng 83 trong file stg/.../store-location-web-mssql/.../appsettings.json thành "ApisUrl": "https://place-api-stg4.concung.vn/" và sau khi sửa xong khoan test liền, đợi 15 phút hả run lại test cho cci-store-location-web
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-18T21:25:42+07:00.

The user's current state is as follows:
Active Document: e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
Cursor is on line: 68
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\e2e\output-sale-lucky-draw-reward-points\output-sale-lucky-draw-reward-points.e2e.spec.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
</ADDITIONAL_METADATA>

---

## 15. 19/10/2026 09:48

<USER_REQUEST>
chạy sub agent giải quyết song song 2 vấn đề bên trên
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T09:48:47+07:00.

The user's current state is as follows:
Other open documents:
- e:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\chain-net10.ps1 (LANGUAGE_POWERSHELL)
- e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\e2e\output-sale-lucky-draws\output-sale-lucky-draws.e2e.spec.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\e2e\output-sale-lucky-draw-reward-points\output-sale-lucky-draw-reward-points.e2e.spec.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\GIT_RULES.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 16. 19/10/2026 11:50

<USER_REQUEST>
- Update rule global không cần đợi tôi click tạo PR nữa, cần thì bạn tạo PR luôn không cần đợi confirm create, chỉ cần đưa lại link
- lỗi 500 bên trên của SCM kiểm tra tại sao stg4 không gặp lỗi tương tự như stg10, stg4 giường như là code của thư mục origin còn stg10 là target, kiểm tra nguyên nhân, chưa fix
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T11:50:29+07:00.

The user's current state is as follows:
Other open documents:
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draw-reward-points.page.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\chain-net10.ps1 (LANGUAGE_POWERSHELL)
- e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\e2e\output-sale-lucky-draws\output-sale-lucky-draws.e2e.spec.ts (LANGUAGE_TYPESCRIPT)
</ADDITIONAL_METADATA>

---

## 17. 19/10/2026 12:44

<USER_REQUEST>
- chạy test lại cho cci-store-location-web vì lỗi bên trên đã được fix
- fix lỗi cho scm và tạo PR,kiểm tra tình trạng đó ở chung dc và store-location luôn nha, rule global phải luôn được nạp lại và làm đúng
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T12:44:05+07:00.

The user's current state is as follows:
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_UNSPECIFIED)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draws.page.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draw-reward-points.page.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\chain-net10.ps1 (LANGUAGE_POWERSHELL)
</ADDITIONAL_METADATA>

---

## 18. 19/10/2026 12:51

<USER_REQUEST>
- chạy 1 background agent test tiếp tục cho 2 portal trên, phần scm sẽ đợi 10p  rồi mới tiếp tục vì đang deploy
- chạy 1 background đi lấy commit của 2 repo https://bitbucket.org/concung/cci-hrm-web và @[e:\Work\Place_Migrate\cci-mbm-web] fetch pull mới nhất nhánh dev về và list các commit fix bug cũng như là dev đã fix gì build gì cho nó để đem về dập khuôn cho 3 project mà chúng ta đang làm là dc,store-location và scm (lưu ý là tất cả các commit nên để tránh việc fix trùng và dư thừa thì nên list lại sau đó gom nhóm, phân loại và kiểm tra xem project của chúng ta có gặp vấn đề tương tự không rồi mới đi dập khuôn vào chứ không phải cứ kéo về áp dụng tất cả.)
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T12:51:18+07:00.

The user's current state is as follows:
Other open documents:
- e:\Work\Place_Migrate\GIT_RULES.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\scripts\sweep-scm-failfast.ps1 (LANGUAGE_POWERSHELL)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_UNSPECIFIED)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draws.page.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draw-reward-points.page.ts (LANGUAGE_TYPESCRIPT)

The user has mentioned some items in the form @[ITEM]. Here is extra information about the items that were mentioned by the user, in the order that they appear:

@[e:\Work\Place_Migrate\cci-mbm-web] is a [File]:
e:\Work\Place_Migrate\cci-mbm-web
</ADDITIONAL_METADATA>

---

## 19. 19/10/2026 13:14

<USER_REQUEST>
Phần nào kiến nghị và phân tích càn dập khuôn thì dập cho 3 portal web của chúng ta vì đều là deploy chung một môi trường và cung version .net
Phần redis kiểm tra xem nếu HRM làm đúng và project của chúng ta từng thấy nó sai và sửa tạm bợ cho nó chạy thì giờ chúng ta phải sửa nó theo HRM
Giờ chúng ta sẽ tiếp tục build workflow hoàn thiện dựa theo các file global của chúng ta luôn tuân thủ, và chạy ngầm dưới backgorund test các portal nếu còn phát hiện lỗi migrate -> kiểm tra nguyên nhân, phân loại, xác định vấn đề là cần người fix hay là tự đi fix được -> nếu tự đi fix được thì đi fix xong sau đó theo rule global push commit và làm đúng quy trình sau đó đợi 15p chạy lại test case rồi tiếp tục tìm vấn đề và fix cho đến khi migrate đạt 100% không lỗi migrate. Tạo 1 job cứ mỗi 5h chiều hằng ngày thì chạy workflow kéo hết commit nhánh dev như bên trên của 2 repo hrm và mbm web đi list commit phân tích hiện trạng với 3 project của chúng ta và phân tích có dập khuôn không và tiến hành dập khuôn nếu có commit thì commit lên rồi làm theo rule tiếp tục, ưu tiên chạy bằng background hết để khung chat trống có thể prompt giữa chừng mà không bị gián đoạn, ý tôi ở đây là ưu tiên tuyệt đối sub agent, bạn bổ sung tất cả context này vào rule global và tạo workflow tự động có thể chạy xuyên suốt cho đến khi migrate thành công.

</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T13:14:44+07:00.

The user's current state is as follows:
Other open documents:
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draws.page.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\pages\output-sale-lucky-draw-reward-points.page.ts (LANGUAGE_TYPESCRIPT)
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\03_qa\scripts\chain-net10.ps1 (LANGUAGE_POWERSHELL)
- e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
</ADDITIONAL_METADATA>

---

## 20. 19/10/2026 13:30

<USER_REQUEST>
đã dập khuôn từ các portal bên trên xong chưa, đã dập được những gì và nếu có thì đã push lên chưa
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T13:30:28+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 33
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 21. 19/10/2026 13:34

<USER_REQUEST>
1. clone repo này về workspace git clone https://tinhkun102@bitbucket.org/concung/cci-hrm-api.git
2. Tiến hành dập khuôn và up code
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T13:34:53+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 33
Other open documents:
- e:\Work\Place_Migrate\AGENTS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\dev-ops\vaults-gitops\stg\cci\store-location\store-location-web-mssql\configs\appsettings.json (LANGUAGE_JSON)
</ADDITIONAL_METADATA>

---

## 22. 19/10/2026 14:38

<USER_REQUEST>
cci-store-location-web sau khi push cũng phải chạy lại test case
tiếp tục lấy commit của các repo sau đây về để tiến hành phân tích nhóm lỗi và dập khuôn cho 3 project bên trên: https://bitbucket.org/concung/cci-timekeeping-web, https://bitbucket.org/concung/cci-supplier-web, https://bitbucket.org/concung/cci-common-web -> Thêm phần này vào rule 17:00 mà chúng ta set ở lúc nảy luôn
tức là sau mỗi lần dập khuôn vẫn phải chạy lại test case cho phần dập khuôn đó, không cần phải chạy hết test case từ đầu, phần dập khuôn đó ảnh hưởng phần gì và kích hoạt test case cho phần đó thôi
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T14:38:06+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\cci-hrm-api\03_qa\ROW-SCHEMA.md (LANGUAGE_MARKDOWN)
Cursor is on line: 22
Other open documents:
- e:\Work\Place_Migrate\cci-hrm-api\03_qa\ROW-SCHEMA.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 23. 19/10/2026 14:58

<USER_REQUEST>
thấy trạng thái của cci-dc-web là "✅ Parity 100%
(NET4: 373P/383S/1F
NET10: 375P/381S/1F)" còn của cci-store-location-web là "✅ FULL TEST NET10 MSSQL — PARITY VƯỢT NET4
• NET4: 487P / 57S / 15F (ID 634)
• NET10: 507P / 39S / 13F (ID 652)
• Targeted Test Sau Dập Khuôn: 33P / 1S / 0F (100% PASS)"
có vẻ như cci-dc-web đang bị test hoặc dập khuôn thiếu thì phải 
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T14:58:58+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 24. 19/10/2026 15:12

<USER_REQUEST>
chạy job ngay bây giờ luôn, không cần đợi 17h hôm nay, tạm thời hôm nay chạy trước
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T15:12:28+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 25. 19/10/2026 15:20

<USER_REQUEST>
lưu ý là lần này là lần đầu tiên chạy job nên phải kéo tất cả commit của ông dev khi bắt đầu fix chứ không phải giới hạn ngày nha, các job hôm sau mới bắt đầu là kéo commit trong ngày, cập nhật rule và xem đã chạy đúng như trên chưa
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T15:20:01+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 26. 19/10/2026 15:25

<USER_REQUEST>
có gì để dập khuôn không
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T15:25:40+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 27. 19/10/2026 15:31

<USER_REQUEST>
vậy sau khi dập khuôn đã apply được gì chưa, có commit mới không
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T15:31:10+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 11
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 28. 19/10/2026 15:41

<USER_REQUEST>
mong muốn trong phần rule này mỗi lần fix một lỗi gì đó hoặc dập khuôn từ các project khác thì phân loại nhóm lỗi ra và mô tả là đã fix được gì, sau mỗi lần fix bug và test case phải bổ sung lỗi đó và phân nhóm để gắn thêm vào report. Trong workspace đó mỗi lần chạy xong sẽ up kết quả test lên portal report, 1 bản trên server và có cả bản report local . Mong muốn upgrade bản report local (chưa đụng tới phần sửa report ngoài việc push thêm data lên server) thêm cho phần report local nhóm lỗi phân loại lỗi bên trên và tình trạng fix, fix được gì, compare được cái cũ viết như thế nào mà lỗi còn cái mới viết như thế nào mà lỗi, gom tất cả commit fix bug của phần dc và build thêm cho tool report giúp tôi, trước tiên là chúng ta build cho cci-store-location-web trước khi triển khai cả 3 portal
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T15:41:46+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 14
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 29. 19/10/2026 15:53

<USER_REQUEST>
cho tôi xem port của report local để tôi mở xem thử
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T15:53:44+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 14
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 30. 19/10/2026 16:03

<USER_REQUEST>
tôi thấy web report trên server đang UI như hình 1 mà, sao bạn chạy http://localhost:8080/ lên như hình 2 nhìn khác vậy có chạy nhầm không
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T16:03:01+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 14
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 31. 19/10/2026 16:08

<USER_REQUEST>
UI như này là đúng, và phần report nhóm lỗi vừa rồi phải được gắn trên nó mới đúng, bạn đừng dùng tool thao tác browser, hiện tại phần đó của bạn hoạt động chưa tốt nên không cần
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T16:08:36+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 14
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 32. 19/10/2026 16:30

<USER_REQUEST>
chưa thấy phần thay đổi code này
và phần UI phải làm 1 map tổng để xem trực quan thay vì phải kéo để xem nhóm lỗi, và UI phải mô tả được nhóm lỗi đó là gì và nguyên nhân 
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T16:30:43+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 14
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 33. 19/10/2026 16:43

<USER_REQUEST>
E:\Work\Place_Migrate\cci-scm-web\00_docs\PLAN_PARITY_COMPARE_LOCAL_REPORT.md và work chạy trước cho phần cci-store-location
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T16:43:37+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 14
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 34. 19/10/2026 17:10

<USER_REQUEST>
Lỗi khiến [Store Location Web — Test Report Viewer](http://localhost:8932/) không lên UI

app.js?v=20260930h:1255 Uncaught ReferenceError: renderParityTab is not defined
    at renderAll (app.js?v=20260930h:1255:5)
    at app.js?v=20260930h:1410:3
    at app.js?v=20260930h:1411:3
renderAll @ app.js?v=20260930h:1255
(anonymous) @ app.js?v=20260930h:1410
(anonymous) @ app.js?v=20260930h:1411
inject_jquery.js:1 [Violation] Permissions policy violation: unload is not allowed in this document.
ie.setDocument @ inject_jquery.js:1
ie @ inject_jquery.js:1
find @ inject_jquery.js:1
(anonymous) @ reformat.js:1
setInterval
(anonymous) @ reformat.js:1
t.createFrame @ reformat.js:1
t.getReformat @ reformat.js:1
(anonymous) @ content-script.js:1
u @ inject_jquery.js:1
fireWith @ inject_jquery.js:1
ready @ inject_jquery.js:1
_ @ inject_jquery.js:1

</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T17:10:59+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
Cursor is on line: 488
Other open documents:
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\03_qa\scripts\wait-and-sweep.ps1 (LANGUAGE_POWERSHELL)
</ADDITIONAL_METADATA>

---

## 35. 19/10/2026 17:19

<USER_REQUEST>
asset:1  GET http://localhost:8932/api/asset?path=E%3A%5CWork%5CPlace_Migrate%5Ccci-store-location-web%5C03_qa%5Ctest-results%5Ce2e-location-edit-location-b4beb-orm-s%E1%BB%ADa-m%E1%BA%B7t-b%E1%BA%B1ng-9612-LOAD--e2e%5Ctest-failed-1.png 404 (not found)
Image
renderTestDetail @ app.js?v=20261019i:813
renderDetail @ app.js?v=20261019i:860
renderAll @ app.js?v=20261019i:1582
(anonymous) @ app.js?v=20261019i:1734
(anonymous) @ app.js?v=20261019i:1735
inject_jquery.js:1 [Violation] Permissions policy violation: unload is not allowed in this document.
ie.setDocument @ inject_jquery.js:1
ie @ inject_jquery.js:1
find @ inject_jquery.js:1
(anonymous) @ reformat.js:1
setInterval
(anonymous) @ reformat.js:1
t.createFrame @ reformat.js:1
t.getReformat @ reformat.js:1
(anonymous) @ content-script.js:1
u @ inject_jquery.js:1
fireWith @ inject_jquery.js:1
ready @ inject_jquery.js:1
_ @ inject_jquery.js:1


và cũng chưa thấy được phần playright lấy param so sánh, không thấy được phần đó về mặt UI
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T17:19:57+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
Cursor is on line: 478
Other open documents:
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-store-location-web\.report\viewer\index.html (LANGUAGE_HTML)
</ADDITIONAL_METADATA>

---

## 36. 19/10/2026 20:23

<USER_REQUEST>
phần scm chạy dưới background xong chưa
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T20:23:12+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 56
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
</ADDITIONAL_METADATA>

---

## 37. 19/10/2026 20:32

<USER_REQUEST>
[Store Location Web — Test Report Viewer](http://localhost:8932/) phần này các UI khác không đổi nha, giữ nguyên tất cả, chỉ làm thêm phần compare các thứ như trong plant thôi, phần nào không yêu cầu thì giữ nguyên, ví dụ như table dimension ở chi tiết đã bị xóa mất, trả lại như cũ, giống như làm thêm để đưa leader tham khảo có chốt không, phần cũ thì vẫn phải để đó
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T20:32:29+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 56
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
</ADDITIONAL_METADATA>

---

## 38. 19/10/2026 20:41

<USER_REQUEST>
phần payload param compare ở đâu vậy trên UI
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T20:41:06+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 56
Other open documents:
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 39. 19/10/2026 20:46

<USER_REQUEST>
tôi không thấy resquest và response
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T20:46:23+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 56
Other open documents:
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
</ADDITIONAL_METADATA>

---

## 40. 19/10/2026 20:58

<USER_REQUEST>
lưu ý là request và response không giả định code mà có nha, phải được lấy từ kết quả của playright
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T20:58:55+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 56
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
</ADDITIONAL_METADATA>

---

## 41. 19/10/2026 21:35

<USER_REQUEST>
[Mặt bằng - Danh sách tuyến đường](https://place-stg10.concung.vn/mat-bang/danh-sach-tuyen-duong)

kiểm tra xem page này là cái nào để tôi đi xem nó test
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-10-19T21:35:53+07:00.

The user's current state is as follows:
Active Document: e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
Cursor is on line: 56
Other open documents:
- e:\Work\Place_Migrate\WORKSPACE_PROGRESS.md (LANGUAGE_MARKDOWN)
- e:\Work\Place_Migrate\cci-scm-web\02_target\CoC.Web.SCM\Controllers\OutputUsesController.cs (LANGUAGE_CSHARP)
</ADDITIONAL_METADATA>

---

## 42. 19/10/2026 21:39

<USER_REQUEST>
sao thấy bộ test để là rỗng, còn tôi thử lên search tay thì nó ra data như thế này {
    "objCodeStep": {
        "Status": "Success",
        "Message": null,
        "SuccessStep": "https://place-api-stg4.concung.vn/api/Routes/Search",
        "ErrorStep": "Read Response",
        "ErrorMessage": "",
        "Data": [
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 828,
                "PlaceName": "Quảng Trường Lam Sơn/Nhà hát Lam Sơn Thanh Hóa",
                "RPID": 3235,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Đông Thọ",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 869,
                "PlaceName": "TGDĐ - 344 Trường Thi (Thanh Hóa)",
                "RPID": 3236,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Điện Biên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 2234,
                "PlaceName": "Tượng đài Lê Lợi Thanh Hóa",
                "RPID": 3237,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Điện Biên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 92,
                "PlaceName": "Bệnh viện Đa khoa TP Thanh Hóa",
                "RPID": 3238,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Lam Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 101,
                "PlaceName": "Bệnh viện Nhi Thanh Hóa",
                "RPID": 3239,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Lam Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 1018,
                "PlaceName": "Vincom Plaza Trần Phú Thanh Hóa",
                "RPID": 3241,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Lam Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 639,
                "PlaceName": "FPT 175 Trần Phú Thanh Hóa",
                "RPID": 3240,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Thanh Hóa",
                "WardName": "Phường Lam Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6098,
                "PlaceName": "TGDĐ Trần Phú",
                "RPID": 3193,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thị Xã Bỉm Sơn",
                "WardName": "Phường Bắc Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6099,
                "PlaceName": "Bệnh viện đa khoa Sầm Sơn",
                "RPID": 3230,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Sầm Sơn",
                "WardName": "Phường Trung Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6100,
                "PlaceName": "Điện Máy Xanh 91 Lê Lợi, TX Sầm Sơn",
                "RPID": 3231,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thành Phố Sầm Sơn",
                "WardName": "Phường Trung Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6439,
                "PlaceName": "Chợ Mường Lát",
                "RPID": 3210,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Mường Lát",
                "WardName": "Thị Trấn Mường Lát",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6101,
                "PlaceName": "Bêệnh viện đa khoa Quan Hóa",
                "RPID": 3224,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Quan Hóa",
                "WardName": "Thị Trấn Quan Hóa",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6102,
                "PlaceName": "Điện Máy Xanh TT Cành Nàng",
                "RPID": 3191,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Bá Thước",
                "WardName": "Thị Trấn Cành Nàng",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6103,
                "PlaceName": "Điện Máy Xanh xã Điền Lư",
                "RPID": 3192,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Bá Thước",
                "WardName": "Xã Điền Lư",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6104,
                "PlaceName": "Ngã 3 đường 217",
                "RPID": 3225,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Quan Sơn",
                "WardName": "Thị Trấn Quan Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6105,
                "PlaceName": "Ngã 4 Châu Lang - Lang CHánh",
                "RPID": 3209,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Lang Chánh",
                "WardName": "Thị Trấn Lang Chánh",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6106,
                "PlaceName": "Điện Máy Xanh 17B Lê Thánh Tông, TT Ngọc Lặc",
                "RPID": 3214,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Ngọc Lặc",
                "WardName": "Thị Trấn Ngọc Lặc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6107,
                "PlaceName": "TGDĐ 02 Lê Lai, TT Ngọc Lặc",
                "RPID": 3215,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Ngọc Lặc",
                "WardName": "Thị Trấn Ngọc Lặc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6108,
                "PlaceName": "TGDĐ Ngọc Lặc",
                "RPID": 3216,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Ngọc Lặc",
                "WardName": "Thị Trấn Ngọc Lặc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6109,
                "PlaceName": "Chợ Cẩm Sơn",
                "RPID": 3194,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Cẩm Thủy",
                "WardName": "Thị Trấn Cẩm Thủy",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6110,
                "PlaceName": "Điện Máy Xanh Thôn Đại Đồng, Xã Cẩm Sơn, H. Cẩm Thuỷ",
                "RPID": 3195,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Cẩm Thủy",
                "WardName": "Xã Cẩm Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6111,
                "PlaceName": "Chợ Kim Tân",
                "RPID": 3232,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thạch Thành",
                "WardName": "Thị Trấn Kim Tân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6112,
                "PlaceName": "Điện Máy Xanh TT Kim Tân",
                "RPID": 3233,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thạch Thành",
                "WardName": "Thị Trấn Kim Tân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6113,
                "PlaceName": "TGDĐ Vân Du",
                "RPID": 3234,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thạch Thành",
                "WardName": "Thị Trấn Vân Du",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 702,
                "PlaceName": "FPT Số 1 Cổng Chợ Lèn Thanh Hóa",
                "RPID": 3198,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hà Trung",
                "WardName": "Xã Hà Phong",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6114,
                "PlaceName": "Bệnh viện đa khoa Hà Trung",
                "RPID": 3199,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hà Trung",
                "WardName": "Xã Hà Ninh",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6116,
                "PlaceName": "Chợ Giáng",
                "RPID": 3262,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Vĩnh Lộc",
                "WardName": "Thị Trấn Vĩnh Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6115,
                "PlaceName": "Bệnh viện Đa Khoa Vĩnh Lộc",
                "RPID": 3261,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Vĩnh Lộc",
                "WardName": "Thị Trấn Vĩnh Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6117,
                "PlaceName": "Chợ Quán Lào",
                "RPID": 3263,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Yên Định",
                "WardName": "Thị Trấn Quán Lào",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6118,
                "PlaceName": "Điện Máy Xanh Quán Lào",
                "RPID": 3264,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Yên Định",
                "WardName": "Thị Trấn Quán Lào",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6119,
                "PlaceName": "Điện Máy Xanh Phố Kiểu",
                "RPID": 3265,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Yên Định",
                "WardName": "Xã Yên Trường",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6120,
                "PlaceName": "Điện Máy Xanh Thọ Xuân",
                "RPID": 3245,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thọ Xuân",
                "WardName": "Thị Trấn Thọ Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6121,
                "PlaceName": "Điện Máy Xanh TT Lam Sơn",
                "RPID": 3246,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thọ Xuân",
                "WardName": "Thị Trấn Lam Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6122,
                "PlaceName": "Điện Máy Xanh Sao Vàng",
                "RPID": 3247,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thọ Xuân",
                "WardName": "Thị Trấn Sao Vàng",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6123,
                "PlaceName": "Điện Máy Xanh Thọ Hải",
                "RPID": 3248,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thọ Xuân",
                "WardName": "Xã Thọ Hải",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6124,
                "PlaceName": "Ngã 3 Cầm Bá Thước - Lê Lợi",
                "RPID": 3249,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thường Xuân",
                "WardName": "Thị Trấn Thường Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6125,
                "PlaceName": "QL 47 giao Như Thanh",
                "RPID": 3250,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thường Xuân",
                "WardName": "Thị Trấn Thường Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 698,
                "PlaceName": "FPT Phố Giắt - Triệu Sơn Thanh Hóa",
                "RPID": 3259,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Triệu Sơn",
                "WardName": "Thị Trấn Triệu Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6126,
                "PlaceName": "Điện Máy Xanh Hợp Thành",
                "RPID": 3257,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Triệu Sơn",
                "WardName": "Xã Hợp Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6127,
                "PlaceName": "Điện Máy Xanh Thị Trấn Nưa",
                "RPID": 3258,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Triệu Sơn",
                "WardName": "Xã Hợp Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6128,
                "PlaceName": "Điện Máy Xanh Thọ Dân",
                "RPID": 3260,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Triệu Sơn",
                "WardName": "Xã Thọ Dân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6129,
                "PlaceName": "TGDĐ 198 Quốc Lộ 45",
                "RPID": 3242,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thiệu Hoá",
                "WardName": "Thị Trấn Vạn Hà",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6130,
                "PlaceName": "Bệnh viện đa khoa Thiệu Hóa",
                "RPID": 3243,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thiệu Hoá",
                "WardName": "Xã Thiệu Đô",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6131,
                "PlaceName": "TGDĐ Xã Thiệu Đô",
                "RPID": 3244,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Thiệu Hoá",
                "WardName": "Xã Thiệu Đô",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6132,
                "PlaceName": "Chợ Hoằng Giang",
                "RPID": 3204,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hoằng Hóa",
                "WardName": "Xã Hoằng Giang",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6133,
                "PlaceName": "Chợ Gốc Cáo",
                "RPID": 3205,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hoằng Hóa",
                "WardName": "Xã Hoằng Phú",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6134,
                "PlaceName": "Điện Máy Xanh Hoằng Kim",
                "RPID": 3206,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hoằng Hóa",
                "WardName": "Xã Hoằng Kim",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6135,
                "PlaceName": "Điện Máy Xanh Hoằng Lộc",
                "RPID": 3207,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hoằng Hóa",
                "WardName": "Xã Hoằng Kim",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6136,
                "PlaceName": "Chợ Gòng",
                "RPID": 3208,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hoằng Hóa",
                "WardName": "Xã Hoằng Phúc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6141,
                "PlaceName": "Chợ Hậu Lộc",
                "RPID": 3200,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hậu Lộc",
                "WardName": "Thị Trấn Hậu Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6142,
                "PlaceName": "Điện Máy Xanh TT Hậu Lộc",
                "RPID": 3201,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hậu Lộc",
                "WardName": "Thị Trấn Hậu Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6143,
                "PlaceName": "Điện máy HC",
                "RPID": 3202,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hậu Lộc",
                "WardName": "Xã Hoa Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6144,
                "PlaceName": "Điện Máy Xanh Minh Lộc",
                "RPID": 3203,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Hậu Lộc",
                "WardName": "Xã Minh Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6145,
                "PlaceName": "Điện Máy Xanh Nga Sơn",
                "RPID": 3211,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nga Sơn",
                "WardName": "Thị Trấn Nga Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6146,
                "PlaceName": "TGDĐ số 152 tiểu Khu 3, TT Nga Sơn",
                "RPID": 3212,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nga Sơn",
                "WardName": "Thị Trấn Nga Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6147,
                "PlaceName": "Điện Máy Xanh xã Nga Thanh",
                "RPID": 3213,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nga Sơn",
                "WardName": "Xã Nga Thanh",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6148,
                "PlaceName": "Bênh viện Đa Khoa Như Xuân",
                "RPID": 3219,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Như Xuân",
                "WardName": "Thị Trấn Yên Cát",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6149,
                "PlaceName": "Bệnh viện đa khoa huyện Như Thanh",
                "RPID": 3217,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Như Thanh",
                "WardName": "Thị Trấn Bến Sung",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6150,
                "PlaceName": "Điện Máy Xanh TT Bến Sung",
                "RPID": 3218,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Như Thanh",
                "WardName": "Thị Trấn Bến Sung",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6151,
                "PlaceName": "Điện Máy Xanh TT Đông Hoà",
                "RPID": 3220,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nông Cống",
                "WardName": "Xã Trung Chính",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6152,
                "PlaceName": "Điện Máy Xanh xã Trunh Chính",
                "RPID": 3221,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nông Cống",
                "WardName": "Xã Trung Chính",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6153,
                "PlaceName": "Chợ Minh Thọ, Hồng Phi thế giới bỉm sữa",
                "RPID": 3222,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nông Cống",
                "WardName": "Xã Minh Thọ",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6154,
                "PlaceName": "Điện Máy Xanh Xã Minh Khôi",
                "RPID": 3223,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Nông Cống",
                "WardName": "Xã Minh Khôi",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6155,
                "PlaceName": "Chợ Cầu Đống",
                "RPID": 3196,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Đông Sơn",
                "WardName": "Thị Trấn Rừng Thông",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6156,
                "PlaceName": "Ngã 3 QL 45 - Nguyễn Mộng Tuân",
                "RPID": 3197,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Đông Sơn",
                "WardName": "Thị Trấn Rừng Thông",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6138,
                "PlaceName": "Điện Máy Xanh Thị Trấn Quảng Xương",
                "RPID": 3227,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Quảng Xương",
                "WardName": "Thị Trấn Quảng Xương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6140,
                "PlaceName": "Điện Máy Xanh xã Tiên Trang",
                "RPID": 3228,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Quảng Xương",
                "WardName": "Thị Trấn Quảng Xương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6137,
                "PlaceName": "Chợ Quảng Xương",
                "RPID": 3226,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Quảng Xương",
                "WardName": "Thị Trấn Quảng Xương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6139,
                "PlaceName": "Điện Máy Xanh xã Quảng Bình",
                "RPID": 3229,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Quảng Xương",
                "WardName": "Xã Quảng Định",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6157,
                "PlaceName": "Bệnh viện đa khoa khu vực Nghi Sơn",
                "RPID": 3251,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Tĩnh Gia",
                "WardName": "Thị Trấn Tĩnh Gia",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6158,
                "PlaceName": "Bệnh viện đa khoa quốc tế Hợp Lực",
                "RPID": 3252,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Tĩnh Gia",
                "WardName": "Thị Trấn Tĩnh Gia",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6160,
                "PlaceName": "ĐMX 35 Quang Trung",
                "RPID": 3254,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Tĩnh Gia",
                "WardName": "Thị Trấn Tĩnh Gia",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6161,
                "PlaceName": "ĐMX Chợ Trúc",
                "RPID": 3255,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Tĩnh Gia",
                "WardName": "Thị Trấn Tĩnh Gia",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6162,
                "PlaceName": "ĐMX thôn Bắc Hải",
                "RPID": 3256,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Huyện Tĩnh Gia",
                "WardName": "Thị Trấn Tĩnh Gia",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6163,
                "PlaceName": "Điện Máy Xanh 7C Nguyễn Trãi, TP. Vinh",
                "RPID": 3319,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Quán Bàu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6164,
                "PlaceName": "Điện Máy Xanh 78 Nguyễn Thị Minh Khai, TP.Vinh",
                "RPID": 3320,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Hưng Bình",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6165,
                "PlaceName": "TGDĐ 92 Nguyễn Phong Sắc, TP.Vinh",
                "RPID": 3321,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Hưng Dũng",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6166,
                "PlaceName": "Ngã Tư Chợ Vinh",
                "RPID": 3322,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Quang Trung",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 1183,
                "PlaceName": "NAN - 85 Nguyễn Thị Minh Khai",
                "RPID": 3323,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Lê Mao",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 2236,
                "PlaceName": "Bibo Mart số 8 Đinh Công Tráng, Lê Mao, TP Vinh",
                "RPID": 3324,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Lê Mao",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 1182,
                "PlaceName": "NAN - 83 Nguyễn Văn Cừ",
                "RPID": 3325,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Trường Thi",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 2235,
                "PlaceName": "Điện Máy Xanh 218 Lê Duẩn Vinh",
                "RPID": 3326,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thành Phố Vinh",
                "WardName": "Phường Trường Thi",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6167,
                "PlaceName": "Quảng Trường Bình Minh Cửa Lò",
                "RPID": 3270,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thị Xã Cửa Lò",
                "WardName": "Phường Nghi Thủy",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6168,
                "PlaceName": "FPT Shop 180 Trần Hưng Đạo",
                "RPID": 3311,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thị Xã Thái Hòa",
                "WardName": "Phường Hòa Hiếu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6169,
                "PlaceName": "Điện Máy Xanh TT Kim Sơn",
                "RPID": 3297,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quế Phong",
                "WardName": "Thị Trấn Kim Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6170,
                "PlaceName": "Điện Máy Xanh TT Quỳ Châu",
                "RPID": 3298,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳ Châu",
                "WardName": "Thị Trấn Quỳ Châu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6171,
                "PlaceName": "Cầu Mường Xén",
                "RPID": 3285,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Kỳ Sơn",
                "WardName": "Thị Trấn Mường Xén",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6172,
                "PlaceName": "Ngã 3 Xiêng Thù",
                "RPID": 3286,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Kỳ Sơn",
                "WardName": "Thị Trấn Mường Xén",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6173,
                "PlaceName": "Điện Máy Xanh TT Hoà Bình",
                "RPID": 3317,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Tương Dương",
                "WardName": "Thị Trấn Hòa Bình",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6174,
                "PlaceName": "Điện Máy Xanh xã Tam Quang",
                "RPID": 3318,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Tương Dương",
                "WardName": "Xã Tam Quang",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6175,
                "PlaceName": "Chợ Xã Nghĩa Lâm",
                "RPID": 3294,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghĩa Đàn",
                "WardName": "Xã Nghĩa Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6176,
                "PlaceName": "Điện Máy Xanh xã Nghĩa Hội",
                "RPID": 3295,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghĩa Đàn",
                "WardName": "Xã Nghĩa Hội",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6177,
                "PlaceName": "Sân vận động TT Nghĩa Đàn",
                "RPID": 3296,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghĩa Đàn",
                "WardName": "Thị trấn Nghĩa Đàn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6178,
                "PlaceName": "Điện Máy Xanh TT Quỳ Hợp",
                "RPID": 3299,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳ Hợp",
                "WardName": "Thị Trấn Quỳ Hợp",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6179,
                "PlaceName": "TGDĐ xã Tam Hợp",
                "RPID": 3300,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳ Hợp",
                "WardName": "Xã Tam Hợp",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6180,
                "PlaceName": "Điện Máy Xanh xã Nghĩa Xuân",
                "RPID": 3301,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳ Hợp",
                "WardName": "Xã Nghĩa Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6181,
                "PlaceName": "Điện Máy Xanh TT Cầu Giát",
                "RPID": 3302,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳnh Lưu",
                "WardName": "Thị Trấn Cầu Giát",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6182,
                "PlaceName": "TGDĐ TT Cầu Giát",
                "RPID": 3303,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳnh Lưu",
                "WardName": "Thị Trấn Cầu Giát",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6183,
                "PlaceName": "Điện Máy Xanh xã Quỳnh Châu",
                "RPID": 3304,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳnh Lưu",
                "WardName": "Xã Quỳnh Châu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6184,
                "PlaceName": "Điện Máy Xanh xã Quỳnh Thạch",
                "RPID": 3305,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳnh Lưu",
                "WardName": "Xã Quỳnh Thạch",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6185,
                "PlaceName": "Điện Máy Xanh xã Quỳnh Nghĩa",
                "RPID": 3306,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳnh Lưu",
                "WardName": "Xã Quỳnh Nghĩa",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6186,
                "PlaceName": "Điện Máy xanh xã Sơn Hải",
                "RPID": 3307,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Quỳnh Lưu",
                "WardName": "Xã Sơn Hải",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6187,
                "PlaceName": "Điện Máy Xanh TT Con Cuông",
                "RPID": 3268,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Con Cuông",
                "WardName": "Thị Trấn Con Cuông",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6188,
                "PlaceName": "Chợ Cây Chanh",
                "RPID": 3269,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Con Cuông",
                "WardName": "Xã Môn Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6189,
                "PlaceName": "Điện Máy Xanh TT Tân Kỳ",
                "RPID": 3308,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Tân Kỳ",
                "WardName": "Thị Trấn Tân Kỳ",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6190,
                "PlaceName": "Chợ Sen",
                "RPID": 3309,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Tân Kỳ",
                "WardName": "Xã Nghĩa Đồng",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6191,
                "PlaceName": "Điện Máy Xanh xã Nghĩa Hoàn",
                "RPID": 3310,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Tân Kỳ",
                "WardName": "Xã Nghĩa Hoàn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6192,
                "PlaceName": "Điện Máy Xanh TT Anh Sơn",
                "RPID": 3266,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Anh Sơn",
                "WardName": "Thị Trấn Anh Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6193,
                "PlaceName": "Điện Máy Xanh Xã Đỉnh Sơn",
                "RPID": 3267,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Anh Sơn",
                "WardName": "Xã Đỉnh Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6194,
                "PlaceName": "Điện Máy Xanh TT Diễn Châu",
                "RPID": 3271,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Diễn Châu",
                "WardName": "Thị Trấn Diễn Châu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6195,
                "PlaceName": "Chợ Tảo Cũ - Diễn Lâm",
                "RPID": 3272,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Diễn Châu",
                "WardName": "Xã Diễn Lâm",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6196,
                "PlaceName": "Điện Máy Xanh xã Diễn Yên",
                "RPID": 3273,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Diễn Châu",
                "WardName": "Xã Diễn Yên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6197,
                "PlaceName": "Điện Máy Xanh Xã Diện Mỹ",
                "RPID": 3274,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Diễn Châu",
                "WardName": "Xã Diễn Mỹ",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6198,
                "PlaceName": "Điện Máy Xanh xã Diễn Kỷ",
                "RPID": 3275,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Diễn Châu",
                "WardName": "Xã Diễn Kỷ",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6199,
                "PlaceName": "Điện Máy Xanh xã Diễn Xuân",
                "RPID": 3276,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Diễn Châu",
                "WardName": "Xã Diễn Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6200,
                "PlaceName": "Điện Máy Xanh TT Yên Thành",
                "RPID": 3327,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Yên Thành",
                "WardName": "Thị Trấn Yên Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6201,
                "PlaceName": "TGDĐ TT Yên Thành",
                "RPID": 3328,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Yên Thành",
                "WardName": "Thị Trấn Yên Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6202,
                "PlaceName": "Ngã Tư Hợp Thành",
                "RPID": 3329,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Yên Thành",
                "WardName": "Xã Hợp Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6203,
                "PlaceName": "Điện Máy Xanh xã Trung Thành",
                "RPID": 3330,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Yên Thành",
                "WardName": "Xã Trung Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6204,
                "PlaceName": "Chợ Vẹo",
                "RPID": 3331,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Yên Thành",
                "WardName": "Xã Liên Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6205,
                "PlaceName": "Điện Máy Xanh Xã Bảo Thành",
                "RPID": 3332,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Yên Thành",
                "WardName": "Xã Bảo Thành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6207,
                "PlaceName": "FPT Shop TT Đô Lương",
                "RPID": 3278,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Đô Lương",
                "WardName": "Thị Trấn Đô Lương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6206,
                "PlaceName": "Điện Máy Xanh TT Đô Lương",
                "RPID": 3277,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Đô Lương",
                "WardName": "Thị Trấn Đô Lương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6208,
                "PlaceName": "Chợ Lạc Sơn",
                "RPID": 3279,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Đô Lương",
                "WardName": "Xã Lạc Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6209,
                "PlaceName": "Ngã tư đường Khuôn Trù Đại gần nhà xe Lộc Thuỷ",
                "RPID": 3280,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Đô Lương",
                "WardName": "Xã Tân Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6210,
                "PlaceName": "Điện Máy Xanh TT Thanh Chương",
                "RPID": 3312,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Thanh Chương",
                "WardName": "Thị Trấn Thanh Chương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6211,
                "PlaceName": "Chợ Chùa",
                "RPID": 3313,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Thanh Chương",
                "WardName": "Xã Phong Thịnh",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6212,
                "PlaceName": "Chợ Rạng",
                "RPID": 3314,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Thanh Chương",
                "WardName": "Xã Thanh Tiên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6213,
                "PlaceName": "Chợ Cồn Thanh Dương",
                "RPID": 3315,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Thanh Chương",
                "WardName": "Xã Thanh Dương",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6214,
                "PlaceName": "Điện Máy Xanh Xã Võ Liệt",
                "RPID": 3316,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Thanh Chương",
                "WardName": "Xã Võ Liệt",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6215,
                "PlaceName": "Điện Máy Xanh TT Quán Hành",
                "RPID": 3290,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghi Lộc",
                "WardName": "Thị Trấn Quán Hành",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6216,
                "PlaceName": "Chợ Nghi Văn",
                "RPID": 3291,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghi Lộc",
                "WardName": "Xã Nghi Văn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6217,
                "PlaceName": "Điện Máy Xanh xã Nghi Thạch",
                "RPID": 3292,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghi Lộc",
                "WardName": "Xã Nghi Thạch",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6218,
                "PlaceName": "Điện Máy Xanh xã Nghi Xuân",
                "RPID": 3293,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nghi Lộc",
                "WardName": "Xã Nghi Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6219,
                "PlaceName": "Huyện Uỷ Nam Đàn",
                "RPID": 3287,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nam Đàn",
                "WardName": "Thị Trấn Nam Đàn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6220,
                "PlaceName": "Điện Máy Xanh xã Vân Điền",
                "RPID": 3288,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nam Đàn",
                "WardName": "Xã Vân Diên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6221,
                "PlaceName": "Khu di tích Kim Liên",
                "RPID": 3289,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Nam Đàn",
                "WardName": "Xã Kim Liên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6222,
                "PlaceName": "Di tích Xô Viết Nghệ Tĩnh",
                "RPID": 3283,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Hưng Nguyên",
                "WardName": "Thị Trấn Hưng Nguyên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6223,
                "PlaceName": "Chợ Cầu",
                "RPID": 3284,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Huyện Hưng Nguyên",
                "WardName": "Xã Hưng Trung",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 1184,
                "PlaceName": "HTI - 53-55 Trần Phú",
                "RPID": 3341,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Thành Phố Hà Tĩnh",
                "WardName": "Phường Trần Phú",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6226,
                "PlaceName": "ĐMX  89 Trần Phú",
                "RPID": 3342,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Thành Phố Hà Tĩnh",
                "WardName": "Phường Trần Phú",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 2233,
                "PlaceName": "Vincom Plaza Hà Tĩnh",
                "RPID": 3343,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Thành Phố Hà Tĩnh",
                "WardName": "Phường Nam Hà",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6462,
                "PlaceName": "Chợ Hà Tĩnh",
                "RPID": 3344,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Thành Phố Hà Tĩnh",
                "WardName": "Phường Nam Hà",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6227,
                "PlaceName": "ĐMX, TGDĐ 111 QL8A Nam Hồng Hồng Lĩnh",
                "RPID": 3345,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Thị Xã Hồng Lĩnh",
                "WardName": "Phường Nam Hồng",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6228,
                "PlaceName": "Bệnh viện đa khoa huyện Hương Sơn",
                "RPID": 3348,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Hương Sơn",
                "WardName": "Thị Trấn Phố Châu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6229,
                "PlaceName": "ĐMX 189 QL8A Hương Sơn",
                "RPID": 3349,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Hương Sơn",
                "WardName": "Thị Trấn Tây Sơn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6230,
                "PlaceName": "ĐMX Đức Thọ",
                "RPID": 3339,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Đức Thọ",
                "WardName": "Thị Trấn Đức Thọ",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6232,
                "PlaceName": "Dịch vụ cưới Dũng Tâm",
                "RPID": 3359,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Vũ Quang",
                "WardName": "Thị Trấn Vũ Quang",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6233,
                "PlaceName": "Chợ Xuân AN",
                "RPID": 3354,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Nghi Xuân",
                "WardName": "Thị Trấn Xuân An",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6234,
                "PlaceName": "ĐMX khối 7 nghi xuân hà tĩnh",
                "RPID": 3355,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Nghi Xuân",
                "WardName": "Thị Trấn Xuân An",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6235,
                "PlaceName": "Bệnh viện Huyện Can Lộc",
                "RPID": 3336,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Can Lộc",
                "WardName": "Thị Trấn Nghèn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6236,
                "PlaceName": "ĐMX 64 Xô Viết Nghệ Tĩnh TT Nghèn , tgdđ 27 xô viết",
                "RPID": 3337,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Can Lộc",
                "WardName": "Thị Trấn Nghèn",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6237,
                "PlaceName": "Chợ Thanh Lộc",
                "RPID": 3338,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Can Lộc",
                "WardName": "Xã Thanh Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6238,
                "PlaceName": "ĐMX 396 Trần Phú",
                "RPID": 3346,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Hương Khê",
                "WardName": "Thị Trấn Hương Khê",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6239,
                "PlaceName": "FPT Shop khối 8 Hương Khê",
                "RPID": 3347,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Hương Khê",
                "WardName": "Thị Trấn Hương Khê",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6240,
                "PlaceName": "ĐMX 39 Lý tự trọng tổ dân phố số 5, Chợ thạch hà",
                "RPID": 3356,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Thạch Hà",
                "WardName": "Thị Trấn Thạch Hà",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6241,
                "PlaceName": "Trung tâm y tế huyện",
                "RPID": 3357,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Thạch Hà",
                "WardName": "Thị Trấn Thạch Hà",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6242,
                "PlaceName": "Cửa hàng tạp hóa Hà Bách",
                "RPID": 3358,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Thạch Hà",
                "WardName": "Xã Thạch Đài",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6243,
                "PlaceName": "Ngã 4 Nguyễn Biên - Nguyễn Đình Liễn",
                "RPID": 3333,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Cẩm Xuyên",
                "WardName": "Thị Trấn Cẩm Xuyên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6244,
                "PlaceName": "FPT Cẩm Xuyên",
                "RPID": 3334,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Cẩm Xuyên",
                "WardName": "Thị Trấn Cẩm Xuyên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6245,
                "PlaceName": "Ngã 4 Đường 19/5 - Liên Thanh",
                "RPID": 3335,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Cẩm Xuyên",
                "WardName": "Xã Cẩm Nhượng",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6246,
                "PlaceName": "Bệnh viện đa khoa thị xã Kỳ Anh",
                "RPID": 3350,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Kỳ Anh",
                "WardName": "Xã Kỳ Bắc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6248,
                "PlaceName": "Chợ huyện Bình Lộc",
                "RPID": 3352,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Lộc Hà",
                "WardName": "Xã Bình Lộc",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6249,
                "PlaceName": "ĐMX Thị Tứ-Lộc Hà",
                "RPID": 3353,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Huyện Lộc Hà",
                "WardName": "Xã Thạch Châu",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6224,
                "PlaceName": "Điện Máy Xanh phường Quỳnh Xuân",
                "RPID": 3281,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thị Xã Hoàng Mai",
                "WardName": "Phường Quỳnh Xuân",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6225,
                "PlaceName": "Điện Máy Xanh phường Quỳnh Thiện",
                "RPID": 3282,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nghệ An",
                "DistrictName": "Thị Xã Hoàng Mai",
                "WardName": "Xã Quỳnh Liên",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6247,
                "PlaceName": "Vincom Kỳ Anh",
                "RPID": 3351,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Tĩnh",
                "DistrictName": "Thị Xã Kỳ Anh",
                "WardName": "Phường Sông Trí",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 160,
                "RouteName": "X3",
                "Description": null,
                "PlaceID": 6159,
                "PlaceName": "Chợ Còng",
                "RPID": 3253,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thanh Hóa",
                "DistrictName": "Thị xã Nghi Sơn",
                "WardName": "Phường Hải Hòa",
                "QuantityPlace": 168,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 1179,
                "PlaceName": "NBI - 153 Lương Văn Thăng",
                "RPID": 3177,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Đông Thành",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6473,
                "PlaceName": "TGDĐ 173 Lương Văn Thăng",
                "RPID": 3178,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Đông Thành",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 783,
                "PlaceName": "Ngã Ba Tam Giác Thành phố Ninh Bình",
                "RPID": 3176,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Đông Thành",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6472,
                "PlaceName": "FPT Shop 788 Trần Hưng Đạo",
                "RPID": 3179,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Tân Thành",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 535,
                "PlaceName": "Chợ Rồng Ninh Bình",
                "RPID": 3180,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Thanh Bình",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 689,
                "PlaceName": "FPT 953 Trần Hưng Đạo Ninh Bình",
                "RPID": 3181,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Thanh Bình",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 88,
                "PlaceName": "Bệnh Viện Đa Khoa Tỉnh Ninh Bình",
                "RPID": 3182,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Nam Thành",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 825,
                "PlaceName": "Quảng Trường Đinh Tiên Hoàng Ninh Bình",
                "RPID": 3183,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Phường Ninh Khánh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6459,
                "PlaceName": "Go! Ninh Bình",
                "RPID": 3184,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Ninh Bình",
                "WardName": "Xã Ninh Phúc",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 1180,
                "PlaceName": "NBI - 244 Quang Trung",
                "RPID": 3185,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Thành Phố Tam Điệp",
                "WardName": "Phường Bắc Sơn",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6084,
                "PlaceName": "Bến xe khách nho quan, chợ nho quan, BIDV, ĐMX, FPT",
                "RPID": 3173,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Nho Quan",
                "WardName": "Thị Trấn Nho Quan",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6085,
                "PlaceName": "Bệnh viện đa khoa khu vực Nho Quan",
                "RPID": 3174,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Nho Quan",
                "WardName": "Thị Trấn Nho Quan",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6086,
                "PlaceName": "TGDĐ 784 Trại Rào, Nho Quan",
                "RPID": 3175,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Nho Quan",
                "WardName": "Thị Trấn Nho Quan",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6087,
                "PlaceName": "Bệnh viện đa khoa Gia Viễn",
                "RPID": 3166,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Gia Viễn",
                "WardName": "Thị Trấn Me",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6088,
                "PlaceName": "ĐMX, Chợ Me",
                "RPID": 3167,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Gia Viễn",
                "WardName": "Thị Trấn Me",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6089,
                "PlaceName": "Bệnh viện Huyện Hoa Lư, Bệnh viện công an Tỉnh Ninh Bình",
                "RPID": 3168,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Hoa Lư",
                "WardName": "Thị Trấn Thiên Tôn",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 1181,
                "PlaceName": "NBI - Phố 3",
                "RPID": 3186,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Yên Khánh",
                "WardName": "Thị Trấn Yên Ninh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6090,
                "PlaceName": "Mediamart, F88, minh hằng Baby, UBND huyện",
                "RPID": 3187,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Yên Khánh",
                "WardName": "Thị Trấn Yên Ninh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6091,
                "PlaceName": "Trung tâm y tế huyện Yên Khánh",
                "RPID": 3188,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Yên Khánh",
                "WardName": "Thị Trấn Yên Ninh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6092,
                "PlaceName": "Bệnh viện đa khoa huyện Kim Sơn",
                "RPID": 3169,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Kim Sơn",
                "WardName": "Thị Trấn Phát Diệm",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6093,
                "PlaceName": "FPT 20 phố Trì Chính",
                "RPID": 3170,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Kim Sơn",
                "WardName": "Thị Trấn Phát Diệm",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6094,
                "PlaceName": "KFC chính hiệu, Chợ Năm Dân",
                "RPID": 3171,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Kim Sơn",
                "WardName": "Thị Trấn Phát Diệm",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6095,
                "PlaceName": "TGDĐ Phát Diệm, BIDV",
                "RPID": 3172,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Kim Sơn",
                "WardName": "Thị Trấn Phát Diệm",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6096,
                "PlaceName": "ĐMX, TGDĐ",
                "RPID": 3189,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Yên Mô",
                "WardName": "Thị Trấn Yên Thịnh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6097,
                "PlaceName": "Mediamart, Bệnh viện Đa khoa Yên Mô, Chợ Ngò",
                "RPID": 3190,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Ninh Bình",
                "DistrictName": "Huyện Yên Mô",
                "WardName": "Thị Trấn Yên Thịnh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 423,
                "PlaceName": "Chợ Bo Thái Bình",
                "RPID": 3147,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Thành Phố Thái Bình",
                "WardName": "Phường Bồ Xuyên",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 663,
                "PlaceName": "FPT 355 Lý BônTGDĐ - 1 Quang Trung Thái Bình",
                "RPID": 3148,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Thành Phố Thái Bình",
                "WardName": "Phường Đề Thám",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 1017,
                "PlaceName": "Vincom Plaza Thái Bình",
                "RPID": 3149,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Thành Phố Thái Bình",
                "WardName": "Phường Đề Thám",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 90,
                "PlaceName": "Bệnh viện đa khoa tỉnh Thái Bình/Bệnh viện Đại học Y Thái Bình",
                "RPID": 3150,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Thành Phố Thái Bình",
                "WardName": "Phường Quang Trung",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6457,
                "PlaceName": "Go! Thái Bình",
                "RPID": 3151,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Thành Phố Thái Bình",
                "WardName": "Phường Phú Khánh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6009,
                "PlaceName": "Chợ Cầu",
                "RPID": 3142,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Quỳnh Phụ",
                "WardName": "Thị Trấn Quỳnh Côi",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6008,
                "PlaceName": "Bệnh viện đa khoa Quỳnh Phụ",
                "RPID": 3141,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Quỳnh Phụ",
                "WardName": "Thị Trấn Quỳnh Côi",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6010,
                "PlaceName": "ĐMX 150 Nguyễn Du TT Quỳnh Côi",
                "RPID": 3143,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Quỳnh Phụ",
                "WardName": "Thị Trấn Quỳnh Côi",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6011,
                "PlaceName": "Honda Mạnh Hùng, Chợ Quỳnh Côi",
                "RPID": 3144,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Quỳnh Phụ",
                "WardName": "Thị Trấn Quỳnh Côi",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6012,
                "PlaceName": "TGDĐ số 91 tổ dân phố 7 TT quỳnh côi",
                "RPID": 3145,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Quỳnh Phụ",
                "WardName": "Thị Trấn Quỳnh Côi",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6433,
                "PlaceName": "Chợ Vĩnh Trà",
                "RPID": 3146,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Quỳnh Phụ",
                "WardName": "Thị Trấn An Bài",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6013,
                "PlaceName": "ĐMX Nhân Cầu 2 Thị Trấn Hưng Hà",
                "RPID": 3132,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Hưng Hà",
                "WardName": "Thị Trấn Hưng Hà",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6014,
                "PlaceName": "FPT Khu Nhân Cầu 3 Thị Trấn Hưng Hà",
                "RPID": 3133,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Hưng Hà",
                "WardName": "Thị Trấn Hưng Hà",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6015,
                "PlaceName": "Mediamart, YODY, Viettel Nhân Cầu 1 Thị Trấn Hưng Hà",
                "RPID": 3134,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Hưng Hà",
                "WardName": "Thị Trấn Hưng Hà",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6016,
                "PlaceName": "TGDĐ Khu Nhân Cầu 2 Thị Trấn Hưng Hà",
                "RPID": 3135,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Hưng Hà",
                "WardName": "Thị Trấn Hưng Hà",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6017,
                "PlaceName": "ĐMX  Thị Trấn Hưng Nhân",
                "RPID": 3136,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Hưng Hà",
                "WardName": "Thị Trấn Hưng Nhân",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6018,
                "PlaceName": "ĐMX 253 Bùi Sỹ Tiêm-Đông Hưng",
                "RPID": 3127,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Đông Hưng",
                "WardName": "Thị Trấn Đông Hưng",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6019,
                "PlaceName": "FPT Đông Hưng, Thế Giới Sữa, Chợ Đông Hưng",
                "RPID": 3128,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Đông Hưng",
                "WardName": "Thị Trấn Đông Hưng",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6020,
                "PlaceName": "FPT, Agribank, BIDV",
                "RPID": 3129,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Đông Hưng",
                "WardName": "Thị Trấn Đông Hưng",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6021,
                "PlaceName": "TGDĐ số 22 tổ 8 Đông Hưng",
                "RPID": 3130,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Đông Hưng",
                "WardName": "Thị Trấn Đông Hưng",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6022,
                "PlaceName": "TGDĐ tổ 2 Đông Hưng",
                "RPID": 3131,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Đông Hưng",
                "WardName": "Thị Trấn Đông Hưng",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 878,
                "PlaceName": "TGDĐ - Khu 6 Diêm Điền Thái Bình",
                "RPID": 3152,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Thái Thụy",
                "WardName": "Thị Trấn Diêm Điền",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6023,
                "PlaceName": "Bệnh viện đa khoa huyện Thái Thụy",
                "RPID": 3153,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Thái Thụy",
                "WardName": "Thị Trấn Diêm Điền",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6024,
                "PlaceName": "ĐMX- Khu 8 Diêm Điền Thái Bình",
                "RPID": 3154,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Thái Thụy",
                "WardName": "Thị Trấn Diêm Điền",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6025,
                "PlaceName": "Mediamart-267 khu 6 Diêm Điền Thái Bình, Yody",
                "RPID": 3155,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Thái Thụy",
                "WardName": "Thị Trấn Diêm Điền",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6026,
                "PlaceName": "TGDĐ, ĐMX mini",
                "RPID": 3156,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Thái Thụy",
                "WardName": "Thị Trấn Diêm Điền",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6027,
                "PlaceName": "Chợ Tây Giang",
                "RPID": 3157,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Tiền Hải",
                "WardName": "Thị Trấn Tiền Hải",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6028,
                "PlaceName": "ĐMX 168 phố Tiểu Hoàng - Tiền Hải",
                "RPID": 3158,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Tiền Hải",
                "WardName": "Thị Trấn Tiền Hải",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6029,
                "PlaceName": "FPT 138 Tiểu Hoàng- Tiền Hải",
                "RPID": 3159,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Tiền Hải",
                "WardName": "Thị Trấn Tiền Hải",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6030,
                "PlaceName": "Ngã 3 ông tượng",
                "RPID": 3160,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Tiền Hải",
                "WardName": "Thị Trấn Tiền Hải",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6031,
                "PlaceName": "Bệnh viện đa khoa Kiến Xương",
                "RPID": 3137,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Kiến Xương",
                "WardName": "Thị Trấn Thanh Nê",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6032,
                "PlaceName": "Bờ Hồ Kiến Xương",
                "RPID": 3138,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Kiến Xương",
                "WardName": "Thị Trấn Thanh Nê",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6033,
                "PlaceName": "ĐMX Thanh Nê, Chợ Thanh Nê",
                "RPID": 3139,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Kiến Xương",
                "WardName": "Thị Trấn Thanh Nê",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6034,
                "PlaceName": "TGDĐ QL39B",
                "RPID": 3140,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Kiến Xương",
                "WardName": "Thị Trấn Thanh Nê",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6035,
                "PlaceName": "Chợ Búng",
                "RPID": 3161,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Vũ Thư",
                "WardName": "Thị Trấn Vũ Thư",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6036,
                "PlaceName": "Chợ Thâm",
                "RPID": 3162,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Vũ Thư",
                "WardName": "Thị Trấn Vũ Thư",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6037,
                "PlaceName": "Chợ Thẫm, Trung tâm y tế huyện Vũ Thư, bệnh viện đa khoa",
                "RPID": 3163,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Vũ Thư",
                "WardName": "Thị Trấn Vũ Thư",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6038,
                "PlaceName": "Chợ Mố xã Hồng Lý",
                "RPID": 3164,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Vũ Thư",
                "WardName": "Xã Hồng Lý",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 159,
                "RouteName": "X2",
                "Description": null,
                "PlaceID": 6039,
                "PlaceName": "Cầu Tân Đệ",
                "RPID": 3165,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Thái Bình",
                "DistrictName": "Huyện Vũ Thư",
                "WardName": "Xã Đồng Thanh",
                "QuantityPlace": 64,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 83,
                "PlaceName": "Bệnh Viện Đa khoa Tỉnh Hà Nam",
                "RPID": 3085,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Thành Phố Phủ Lý",
                "WardName": "Phường Lương Khánh Thiện",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 1013,
                "PlaceName": "Vincom Plaza Phủ Lý, Hà Nam",
                "RPID": 3086,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Thành Phố Phủ Lý",
                "WardName": "Phường Minh Khai",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 2232,
                "PlaceName": "FPT 122 Lê Hoàn Phủ Lý Hà Nam",
                "RPID": 3087,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Thành Phố Phủ Lý",
                "WardName": "Phường Lam Hạ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6040,
                "PlaceName": "ĐMX, FPT, VT Store",
                "RPID": 3075,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Thị Xã Duy Tiên",
                "WardName": "Thị Trấn Đồng Văn",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6041,
                "PlaceName": "Bệnh viện đa khoa Duy Tiên",
                "RPID": 3076,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Thị Xã Duy Tiên",
                "WardName": "Xã Trác Văn",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6042,
                "PlaceName": "ĐMX",
                "RPID": 3077,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Thị Xã Duy Tiên",
                "WardName": "Xã Trác Văn",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6043,
                "PlaceName": "Chợ Quế",
                "RPID": 3078,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Kim Bảng",
                "WardName": "Thị Trấn Quế",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6044,
                "PlaceName": "TGDĐ, Head Honda baby mart, Media mart kim bảng",
                "RPID": 3079,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Kim Bảng",
                "WardName": "Thị Trấn Quế",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6430,
                "PlaceName": "Chợ Đồng Hóa",
                "RPID": 3080,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Kim Bảng",
                "WardName": "Xã Đồng Hóa",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6045,
                "PlaceName": "Chợ Non 1357, Trung tâm y tế huyện Thanh Liêm",
                "RPID": 3088,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Thanh Liêm",
                "WardName": "Xã Liêm Tuyền",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6046,
                "PlaceName": "ĐMX Thanh Nguyên",
                "RPID": 3089,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Thanh Liêm",
                "WardName": "Xã Thanh Nguyên",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6047,
                "PlaceName": "Chợ Bình Mỹ",
                "RPID": 3072,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Bình Lục",
                "WardName": "Thị Trấn Bình Mỹ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6048,
                "PlaceName": "ĐMX, FPT",
                "RPID": 3073,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Bình Lục",
                "WardName": "Thị Trấn Bình Mỹ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6435,
                "PlaceName": "Chợ Đô Hai",
                "RPID": 3074,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Bình Lục",
                "WardName": "Xã An Lão",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6049,
                "PlaceName": "Bệnh viện đa khoa huyện Lý Nhân",
                "RPID": 3081,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Lý Nhân",
                "WardName": "Thị Trấn Vĩnh Trụ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6050,
                "PlaceName": "Siêu thị Lan Chi, Chợ Vĩnh Trụ",
                "RPID": 3082,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Lý Nhân",
                "WardName": "Thị Trấn Vĩnh Trụ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6051,
                "PlaceName": "TGDĐ",
                "RPID": 3083,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Lý Nhân",
                "WardName": "Thị Trấn Vĩnh Trụ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6052,
                "PlaceName": "TGDĐ Lý Nhân",
                "RPID": 3084,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Hà Nam",
                "DistrictName": "Huyện Lý Nhân",
                "WardName": "Thị Trấn Vĩnh Trụ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6426,
                "PlaceName": "Hồ Vị Xuyên/Tượng Đài Trần Quốc Tuấn Nam Định",
                "RPID": 3099,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Thành Phố Nam Định",
                "WardName": "Phường Vị Hoàng",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 74,
                "PlaceName": "Bệnh viện Đa Khoa Nam Định/Bệnh Viện Phụ Sản Nam Định",
                "RPID": 3100,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Thành Phố Nam Định",
                "WardName": "Phường Cửa Bắc",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 1135,
                "PlaceName": "FPT Shop 7-9 Điện Biên",
                "RPID": 3101,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Thành Phố Nam Định",
                "WardName": "Phường Cửa Bắc",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 638,
                "PlaceName": "FPT 174 Trần Hưng ĐạoTGDĐ - 157 Trần Hưng Đạo Nam Định",
                "RPID": 3102,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Thành Phố Nam Định",
                "WardName": "Phường Bà Triệu",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6053,
                "PlaceName": "Chợ Mỹ Tho, FPT",
                "RPID": 3103,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Thành Phố Nam Định",
                "WardName": "Phường Bà Triệu",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6440,
                "PlaceName": "Bệnh viện Đa Khoa Huyện Mỹ Lộc",
                "RPID": 3098,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Mỹ Lộc",
                "WardName": "Thị Trấn Mỹ Lộc",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6055,
                "PlaceName": "Mediamart, Ga núi Gôi, agribank vụ bản",
                "RPID": 3116,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Vụ Bản",
                "WardName": "Thị Trấn Gôi",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6056,
                "PlaceName": "TGDĐ, Thế giới sữa chợ Hầu",
                "RPID": 3117,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Vụ Bản",
                "WardName": "Thị Trấn Gôi",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6057,
                "PlaceName": "TGDĐ, VT Store",
                "RPID": 3118,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Vụ Bản",
                "WardName": "Thị Trấn Gôi",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6058,
                "PlaceName": "Bệnh viện đa khoa ý yên",
                "RPID": 3122,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Ý Yên",
                "WardName": "Thị Trấn Lâm",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6059,
                "PlaceName": "Chợ Lâm",
                "RPID": 3123,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Ý Yên",
                "WardName": "Thị Trấn Lâm",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6060,
                "PlaceName": "Honda Vũ Minh 4, GHTK, Công viên khu đô thị",
                "RPID": 3124,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Ý Yên",
                "WardName": "Thị Trấn Lâm",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6061,
                "PlaceName": "Viettel store",
                "RPID": 3125,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Ý Yên",
                "WardName": "Thị Trấn Lâm",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6062,
                "PlaceName": "VP Bank Ý Yên, Agribank",
                "RPID": 3126,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Ý Yên",
                "WardName": "Thị Trấn Lâm",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6063,
                "PlaceName": "Bệnh viện đa khoa nghĩa hưng",
                "RPID": 3109,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nghĩa Hưng",
                "WardName": "Thị Trấn Liễu Đề",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6064,
                "PlaceName": "Điện máy xanh",
                "RPID": 3110,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nghĩa Hưng",
                "WardName": "Thị Trấn Liễu Đề",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6065,
                "PlaceName": "Trung tâm thương mại nghĩa hưng",
                "RPID": 3111,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nghĩa Hưng",
                "WardName": "Thị Trấn Liễu Đề",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6066,
                "PlaceName": "Trường mầm non nghĩa hưng, bưu điện",
                "RPID": 3112,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nghĩa Hưng",
                "WardName": "Thị Trấn Liễu Đề",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6068,
                "PlaceName": "ĐMX",
                "RPID": 3105,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nam Trực",
                "WardName": "Thị Trấn Nam Giang",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6067,
                "PlaceName": "Chợ Viềng",
                "RPID": 3104,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nam Trực",
                "WardName": "Thị Trấn Nam Giang",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6069,
                "PlaceName": "Phòng khám đa khoa việt pháp",
                "RPID": 3106,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nam Trực",
                "WardName": "Thị Trấn Nam Giang",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6432,
                "PlaceName": "ĐMX",
                "RPID": 3107,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nam Trực",
                "WardName": "Xã Nam Dương",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6438,
                "PlaceName": "Chợ Thượng Cũ - Chợ Thượng Mới",
                "RPID": 3108,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Nam Trực",
                "WardName": "Xã Bình Minh",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6070,
                "PlaceName": "Chợ cổ lễ, tgdđ",
                "RPID": 3113,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Trực Ninh",
                "WardName": "Thị Trấn Cổ Lễ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6071,
                "PlaceName": "Chợ cổ lễ, thế giới sữa, phòng khám đa khoa nam đô, mediamart",
                "RPID": 3114,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Trực Ninh",
                "WardName": "Thị Trấn Cổ Lễ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6072,
                "PlaceName": "Viettel store, vp bank, ĐMX",
                "RPID": 3115,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Trực Ninh",
                "WardName": "Thị Trấn Cổ Lễ",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6073,
                "PlaceName": "ĐMX xuân trường",
                "RPID": 3119,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Xuân Trường",
                "WardName": "Thị Trấn Xuân Trường",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6074,
                "PlaceName": "Trung tâm y tế huyện, agribank, bưu điện huyện, tượng đài trường chinh",
                "RPID": 3120,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Xuân Trường",
                "WardName": "Thị Trấn Xuân Trường",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6075,
                "PlaceName": "Chợ bầu  agribank",
                "RPID": 3121,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Xuân Trường",
                "WardName": "Xã Xuân Kiên",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6076,
                "PlaceName": "Bưu điện huyện giao thủy, agribank, chợ thị trấn ngô đồng",
                "RPID": 3090,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Giao Thủy",
                "WardName": "Thị Trấn Ngô Đồng",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6077,
                "PlaceName": "F88, viettel store, ĐMX",
                "RPID": 3091,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Giao Thủy",
                "WardName": "Thị Trấn Ngô Đồng",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6078,
                "PlaceName": "Trung tâm y tế huyện giao thủy",
                "RPID": 3092,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Giao Thủy",
                "WardName": "Thị Trấn Ngô Đồng",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6079,
                "PlaceName": "Biluxury, F88, Bệnh viện đa khoa, trung tâm y tế huyện Hải Hậu",
                "RPID": 3093,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Hải Hậu",
                "WardName": "Thị Trấn Yên Định",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6080,
                "PlaceName": "Chợ cầu đôi",
                "RPID": 3094,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Hải Hậu",
                "WardName": "Thị Trấn Yên Định",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6081,
                "PlaceName": "FPT, ĐMX",
                "RPID": 3095,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Hải Hậu",
                "WardName": "Thị Trấn Yên Định",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6082,
                "PlaceName": "Mediamart, Viettel post, yamaha,MSB",
                "RPID": 3096,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Hải Hậu",
                "WardName": "Thị Trấn Yên Định",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 158,
                "RouteName": "X1",
                "Description": null,
                "PlaceID": 6083,
                "PlaceName": "ĐMX",
                "RPID": 3097,
                "PriorityLevel": 0,
                "ProvinceName": "Tỉnh Nam Định",
                "DistrictName": "Huyện Hải Hậu",
                "WardName": "Thị Trấn Cồn",
                "QuantityPlace": 55,
                "Estimate": 2
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6305,
                "PlaceName": "Chợ Diêm Gỗ",
                "RPID": 3045,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Ngọc Thụy",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 648,
                "PlaceName": "FPT 232 Ngô Gia Tự",
                "RPID": 3046,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Đức Giang",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6386,
                "PlaceName": "KĐT Việt Hưng",
                "RPID": 3047,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Việt Hưng",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 667,
                "PlaceName": "FPT 420 Nguyễn Văn Cừ",
                "RPID": 3048,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Gia Thụy",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 874,
                "PlaceName": "TGDĐ - 392-396 Nguyễn Văn Cừ",
                "RPID": 3050,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Ngọc Lâm",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6383,
                "PlaceName": "TGDĐ 212 Nguyễn Văn Cừ",
                "RPID": 3051,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Ngọc Lâm",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 461,
                "PlaceName": "Chợ Gia Lâm",
                "RPID": 3049,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Ngọc Lâm",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6329,
                "PlaceName": "Bệnh viện Đa Khoa Tâm Anh",
                "RPID": 3052,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Bồ Đề",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6302,
                "PlaceName": "BiBoMart 51 Sài Đồng",
                "RPID": 3053,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Sài Đồng",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 51,
                "PlaceName": "AEOMALL Long Biên",
                "RPID": 3054,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Long Biên",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6276,
                "PlaceName": "KĐT Vinhome RiverSide",
                "RPID": 3055,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Quận Long Biên",
                "WardName": "Phường Thạch Bàn",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6267,
                "PlaceName": "Điện Máy Xanh TT Yên Viên 203-205-207 đường Hà Huy Tập",
                "RPID": 3037,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Thị Trấn Yên Viên",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6387,
                "PlaceName": "Chợ Dốc Lã",
                "RPID": 3038,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Xã Yên Thường",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6259,
                "PlaceName": "Chợ Ninh Hiệp",
                "RPID": 3039,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Xã Ninh Hiệp",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6314,
                "PlaceName": "Điện Máy Xanh xã Phú Thị",
                "RPID": 3040,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Xã Phú Thị",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 645,
                "PlaceName": "FPT 203 Nguyễn Đức Thuận",
                "RPID": 3041,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Thị Trấn Trâu Quỳ",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 751,
                "PlaceName": "Khu Đô Thị Vincom Ocean Park",
                "RPID": 3042,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Xã Đa Tốn",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6272,
                "PlaceName": "Chợ Kiêu Kỵ",
                "RPID": 3043,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Xã Kiêu Kỵ",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6394,
                "PlaceName": "Làng Gốm Bát Tràng",
                "RPID": 3044,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Gia Lâm",
                "WardName": "Xã Bát Tràng",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 873,
                "PlaceName": "TGDĐ - 389 Ngọc Hồi, Thị Trấn Văn Điển",
                "RPID": 3063,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Thanh Trì",
                "WardName": "Thị Trấn Văn Điển",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 1164,
                "PlaceName": "HNI - 150-152-154 Cầu Bươu",
                "RPID": 3064,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Thanh Trì",
                "WardName": "Xã Tân Triều",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 1652,
                "PlaceName": "Khu Đô Thị Đại Thanh",
                "RPID": 3065,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Thanh Trì",
                "WardName": "Xã Thanh Liệt",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6335,
                "PlaceName": "Bệnh Viện Đa Khoa Huyện Thanh Trì",
                "RPID": 3066,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Thanh Trì",
                "WardName": "Xã Tứ Hiệp",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6320,
                "PlaceName": "TGDĐ xã Ngũ Hiệp",
                "RPID": 3067,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Thanh Trì",
                "WardName": "Xã Ngũ Hiệp",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6351,
                "PlaceName": "Chợ Ngọc Hồi",
                "RPID": 3068,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Thanh Trì",
                "WardName": "Xã Ngọc Hồi",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 2065,
                "PlaceName": "ĐMX Mê Linh, Mê Linh Plaza",
                "RPID": 3056,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Thị Trấn Quang Minh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6286,
                "PlaceName": "Vinmart+ Thạch Đà, Bệnh viện đa khoa Mê Linh, ĐMX",
                "RPID": 3057,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Xã Mê Linh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6301,
                "PlaceName": "ĐMX Thôn Xa Mạc, Chợ chiều Xa Mạc",
                "RPID": 3058,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Xã Mê Linh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6307,
                "PlaceName": "TGDĐ Khu 15 Thôn Yên Nhân, VT Store, Hồ Ba Góc",
                "RPID": 3059,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Xã Mê Linh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6353,
                "PlaceName": "ĐMX Thôn Khê Ngoại 1",
                "RPID": 3060,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Xã Mê Linh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6395,
                "PlaceName": "Chợ Thạch Đà, ĐMX Thạch Đà",
                "RPID": 3061,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Xã Mê Linh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 157,
                "RouteName": "P3",
                "Description": null,
                "PlaceID": 6416,
                "PlaceName": "Chợ Chi Đông, Trạm y tế thị trấn Chi Đông",
                "RPID": 3062,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Mê Linh",
                "WardName": "Xã Mê Linh",
                "QuantityPlace": 32,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 2064,
                "PlaceName": "TGDĐ Sóc Sơn, FPT Shop Sóc Sơn",
                "RPID": 3022,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Sóc Sơn",
                "WardName": "Thị Trấn Sóc Sơn",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6323,
                "PlaceName": "Chợ Phố Nỉ",
                "RPID": 3023,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Sóc Sơn",
                "WardName": "Xã Trung Giã",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6372,
                "PlaceName": "Phố Mã",
                "RPID": 3024,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Sóc Sơn",
                "WardName": "Xã Phù Linh",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6374,
                "PlaceName": "Bệnh viện Đa Khoa huyện Sóc Sơn",
                "RPID": 3025,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Sóc Sơn",
                "WardName": "Xã Tiên Dược",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6333,
                "PlaceName": "TGDĐ Xã Mai Đình",
                "RPID": 3026,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Sóc Sơn",
                "WardName": "Xã Mai Đình",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6268,
                "PlaceName": "Điện Máy Xanh xã Phù Lỗ",
                "RPID": 3027,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Sóc Sơn",
                "WardName": "Xã Phù Lỗ",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6340,
                "PlaceName": "Nhà thuốc Hồng Liên 260 Lê Lợi",
                "RPID": 3028,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Lê Lợi",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6415,
                "PlaceName": "Bệnh viện đa khoa Sơn Tây",
                "RPID": 3029,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Lê Lợi",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 540,
                "PlaceName": "Chợ Sơn Tây",
                "RPID": 3030,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Phú Thịnh",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6311,
                "PlaceName": "TGDĐ 173 Ngô Quyền",
                "RPID": 3031,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Ngô Quyền",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 1168,
                "PlaceName": "HNI - 136 Phùng Khắc Khoan",
                "RPID": 3032,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Quang Trung",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6420,
                "PlaceName": "FPT Shop 3 Nguyễn Thái Học",
                "RPID": 3033,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Quang Trung",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 315,
                "PlaceName": "Bibo Mart Sơn Tây: Số 1 - Phố Chùa Thông, P. Sơn Lộc",
                "RPID": 3034,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Sơn Lộc",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6391,
                "PlaceName": "Công ty TNHH thực phẩm Con Đường Xanh",
                "RPID": 3035,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Trung Hưng",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6410,
                "PlaceName": "Chợ Trung Sơn Trầm",
                "RPID": 3036,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Thị Xã Sơn Tây",
                "WardName": "Phường Trung Sơn Trầm",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6260,
                "PlaceName": "Viettel Store, Yamaha Thịnh Phát, Chợ Thương Binh",
                "RPID": 3000,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Đan Phượng",
                "WardName": "Thị Trấn Phùng",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6303,
                "PlaceName": "FPT 155 Tây Sơn",
                "RPID": 3001,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố Hà Nội",
                "DistrictName": "Huyện Đan Phượng",
                "WardName": "Thị Trấn Phùng",
                "QuantityPlace": 38,
                "Estimate": 3
            },
            {
                "Total": 129,
                "RouteID": 156,
                "RouteName": "P2",
                "Description": null,
                "PlaceID": 6341,
                "PlaceName": "Chợ Phùng",
                "RPID": 3002,
                "PriorityLevel": 0,
                "ProvinceName": "Thành Phố 
<truncated 94303 bytes>

NOTE: The output was truncated because it was too long. Use a more targeted query or a smaller range to get the information you need.

---

