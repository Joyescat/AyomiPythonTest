$('#change-email-form').on('submit', function(event) {
  event.preventDefault();
  console.log("form submitted!");
  update_user();
});

function update_user() {
  console.log("update is working!") // sanity check
  $.ajax({
      url: `user/${4}`,
      type: "POST",
      data: {
        email: $('#new-email').val()
      },
      // handle a successful response
      success : function(json) {
        $('#update-email-modal').modal('close');
        console.log(json); // log the returned json to the console
        console.log("success"); // another sanity check
      },
      // handle error
      error : function(xhr, errmsg, err) {
          $('#results').html(`
            <div class='alert-box alert radius' data-alert>
              Oops! We have encountered an error: ${errmsg}
              <a href='#' class='close'>&times;</a>
            </div>
          `);
          console.log(xhr.status + ": " + xhr.responseText);
      }
  });
};
