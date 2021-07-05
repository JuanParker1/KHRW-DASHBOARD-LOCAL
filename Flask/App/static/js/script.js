// Alert Auto Close
$(".alert").delay(3000).slideUp(400, function() {
    $(this).alert('close');
});