 /************************************************
 * Ajax Mail
 ***********************************************/


// (function ($) {
// 	$(document).ready(function () {

// 	  /* ----------------------------------------------------------- */
// 	  /*  AJAX CONTACT FORM
// 		  /* ----------------------------------------------------------- */
  
// 	  $("#contact-form").on("submit", function () {
// 		$(".form-messege").text("Sending...");
  
// 		var form = $(this);
// 		$.ajax({
// 		  url: form.attr("action"),
// 		  method: form.attr("method"),
// 		  data: form.serialize(),
// 		  success: function (result) {
// 			$(".default-form-single-item").css("display", "none");
// 			$("#contact-form").find(".form-messege").addClass("success");
// 			$(".form-messege").text("Message Sent!");
// 		  },
// 		});
// 		this.reset();
// 		return false;
// 	  });
// 	});
  

//   })(jQuery);



$(function() {

	// Get the form.
	var form = $('#contact-form');

	// Get the messages div.
	var formMessages = $('.output_message');

	// Set up an event listener for the contact form.
	$(form).submit(function(e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize the form data.
		var formData = $(form).serialize();

		$(formMessages).text("Sending...");

		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
			data: formData
		})
		.done(function(response) {
			// Make sure that the formMessages div has the 'success' class.
			$(".form-inputs").css("display", "none");
			$(formMessages).removeClass('error');
			$(formMessages).addClass('success');

			// Set the message text.
			$(formMessages).text("Message Sent!");

			// Clear the form.
			$('#contact-form input,#contact-form textarea').val('');
			this.reset();

			if (window.history.replaceState) {
				window.history.replaceState(null, null, window.location.href);
			}
		})
		.fail(function(data) {
			// Make sure that the formMessages div has the 'error' class. 
			$(formMessages).removeClass('success');
			$(formMessages).addClass('error');

			// Set the message text.
			$(formMessages).text('Oops! An error occured and your message could not be sent.');

		});
	});

});
  