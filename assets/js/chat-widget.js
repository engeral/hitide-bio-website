/* 海泰 AI 助手挂件 · 调用 CloudBase 云托管(CloudBase Run)容器后端 POST /chat
   端点默认指向云托管公网域名，上线前把下面 ENDPOINT 换成
   控制台「云托管 → haitide-web-chat-ai → 服务配置 → 公网访问域名」给出的真实地址。
   本地调试：在页面用 <script>window.HITIDE_AI_ENDPOINT='http://192.168.1.184:3000/chat'</script>
   临时覆盖为本地代理即可。 */
(function () {
  var ENDPOINT = window.HITIDE_AI_ENDPOINT || 'https://haitide-web-chat-ai-296443-11-1460003455.sh.run.tcloudbase.com/chat';
  var fab = document.getElementById('htChatFab');
  var panel = document.getElementById('htChatPanel');
  var closeBtn = document.getElementById('htChatClose');
  var body = document.getElementById('htChatBody');
  var input = document.getElementById('htChatInput');
  var sendBtn = document.getElementById('htChatSend');
  var sw = document.querySelector('.ht-chat-switch');
  var line = 'aqua';

  if (!fab) return;

  function open() { panel.hidden = false; input.focus(); }
  function close() { panel.hidden = true; }
  fab.addEventListener('click', function () { panel.hidden ? open() : close(); });
  closeBtn.addEventListener('click', close);

  if (sw) {
    sw.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-line]');
      if (!b) return;
      line = b.getAttribute('data-line');
      Array.prototype.forEach.call(sw.children, function (c) { c.classList.remove('on'); });
      b.classList.add('on');
    });
  }

  function addMsg(role, text) {
    var d = document.createElement('div');
    d.className = 'ht-msg ' + (role === 'me' ? 'ht-me' : (role === 'err' ? 'ht-err' : 'ht-ai'));
    d.textContent = text;
    body.appendChild(d);
    body.scrollTop = body.scrollHeight;
    return d;
  }

  function buildHistory() {
    var msgs = [];
    Array.prototype.forEach.call(body.querySelectorAll('.ht-msg'), function (m) {
      if (m.classList.contains('ht-typing') || m.classList.contains('ht-err')) return;
      var role = m.classList.contains('ht-me') ? 'user' : 'assistant';
      msgs.push({ role: role, content: m.textContent });
    });
    return msgs;
  }

  function send() {
    var text = input.value.trim();
    if (!text || sendBtn.disabled) return;
    var history = buildHistory();
    addMsg('me', text);
    input.value = '';
    var typing = addMsg('typing', '正在思考…');
    typing.classList.add('ht-typing');
    sendBtn.disabled = true;

    var payload = { line: line, messages: history.concat([{ role: 'user', content: text }]) };

    fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (r) {
        return r.json().then(function (d) { return { ok: r.ok, d: d }; });
      })
      .then(function (res) {
        typing.remove();
        if (!res.ok || !res.d.reply) {
          addMsg('err', 'AI 服务返回异常：' + (res.d && res.d.error ? res.d.error : '未知错误'));
        } else {
          addMsg('ai', res.d.reply);
        }
      })
      .catch(function () {
        typing.remove();
        addMsg('err', 'AI 服务未连接（代理未运行或网络不通）。');
      })
      .finally(function () { sendBtn.disabled = false; input.focus(); });
  }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter') send(); });
})();
