$(function() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
  });

  $('#change-email-form').on('submit', function(event) {
    event.preventDefault();
    var id = $(this).attr("data-id");
    update_user(id);
  });

  function update_user(id) {
    $.ajax({
        url: `/user/${id}`,
        type: "POST",
        data: {
          email: $('#new-email').val(),
        },
        // handle a successful response
        success : function(json) {
          if (!json.error_message) {
            $.modal.close();
            $('#user-email').html(json.email)
          } else {
            $('#error-message').html(`
              <div class='alert-danger alert radius' data-alert>
                ${json.error_message}
              </div>
              `);
          }
        },
        // handle error
        error : function(xhr, errmsg, err) {
            $('#results').html(`
              <div class='alert-box alert radius' data-alert>
                Oops! We have encountered an error: ${errmsg}
                <a href='#' class='close'>&times;</a>
              </div>
            `);
            console.error(xhr.status + ": " + xhr.responseText);
        }
    });
  };
});
