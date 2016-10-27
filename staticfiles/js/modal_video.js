// BOOTSTRAP 3.0 - Open YouTube Video Dynamicaly in Modal Window
// Modal Window for dynamically opening videos
$('.video_youtube').on('click', function(e){
  // Store the query string variables and values
	// Uses "jQuery Query Parser" plugin, to allow for various URL formats (could have extra parameters)
	var queryString = $(this).attr('href');
    var video_descricao = $(this).find('.video_desc').text();
    var p_descricao = "<p>" + video_descricao + "</p>";
    // Prevent opening of external page
    e.preventDefault();

    // Variables for iFrame code. Width and height from data attributes, else use default.
    var vidWidth = 853; // default
    var vidHeight = 480; // default
    var iFrameCode = '<iframe width="' + vidWidth + '" height="'+ vidHeight +'" scrolling="no" allowtransparency="true" allowfullscreen="true" src="' + queryString +'?rel=0&wmode=transparent&showinfo=0" frameborder="0"></iframe>';

    // Replace Modal HTML with iFrame Embed
    $('#mediaModal .modal-body').html(iFrameCode + p_descricao);
    // Set new width of modal window, based on dynamic video content
    $('#mediaModal').on('show.bs.modal', function () {
        // Add video width to left and right padding, to get new width of modal window
        var modalBody = $(this).find('.modal-body');
        var modalDialog = $(this).find('.modal-dialog');
        var newModalWidth = vidWidth;
        // newModalWidth += parseInt(modalDialog.css("padding-left")) + parseInt(modalDialog.css("padding-right"));
        newModalWidth += 'px';
        // Set width of modal (Bootstrap 3.0)
        $(this).find('.modal-dialog').css('width', newModalWidth);
        $(this).find('.modal-dialog').css('margin-top', '10%');
        $(this).find('.modal-content').css('border-radius', 0);
        $(this).find('.modal-content').css('height', vidHeight);
        $(this).find('.modal-body').css('padding', 0);
    });

    // Open Modal
    $('#mediaModal').modal();
    $('.modal-backdrop').css('opacity', 0.95);
});

// Clear modal contents on close.
// There was mention of videos that kept playing in the background.
$('#mediaModal').on('hidden.bs.modal', function () {
	$('#mediaModal .modal-body').html('');
});
