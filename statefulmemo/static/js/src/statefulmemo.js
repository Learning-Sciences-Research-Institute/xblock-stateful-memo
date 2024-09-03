/* Javascript for StatefulMemoXBlock. */
function StatefulMemoXBlock(runtime, element) {

    var handlerUrl = runtime.handlerUrl(element, 'update_memo_text');

    $('#memo-text', element).on('input', function(eventObject) {  // Use 'input' event to detect changes
        var memoText = $(this).val();  // Get the current value of the textarea
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"memo_text": memoText}),  // Send the text to the backend
            contentType: "application/json",  // Specify the content type
            success: null
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
