function StatefulMemoXBlock(runtime, element) {
    var memoTextarea = $(element).find('#memo-text');
    var handlerUrl = runtime.handlerUrl(element, 'update_memo_text');
    var updateTimeout;

    function updateMemo(memoText) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"memo_text": memoText}),
            success: function(response) {
                if (response.memo_text !== memoText) {
                    memoTextarea.val(response.memo_text);
                }
            }
        });
    }

    function debouncedUpdate() {
        clearTimeout(updateTimeout);
        updateTimeout = setTimeout(function() {
            updateMemo(memoTextarea.val());
        }, 500); // Wait for 0.5 second of inactivity before updating
    }

    memoTextarea.on('input', debouncedUpdate);

    $(function ($) {
        updateMemo(memoTextarea.val());
    });
}