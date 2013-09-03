// Taken from http://stackoverflow.com/a/680252/1691611.
function reset_form($form) {
  $form.find('input:text, input:password, input:file, input[type=number], select, textarea').val('');
  $form.find('input:radio, input:checkbox')
    .removeAttr('checked').removeAttr('selected');
}

function truncate(elem, length) {
  elem = $(elem);
  elem.text(elem.text().substring(0, length) + '...');
  elem.data('truncated', true);
}

function untruncate(elem, full_text_key) {
  elem = $(elem);
  elem.text(elem.data(full_text_key));
  elem.data('truncated', false);
}

$(function() {
  // Configure table sorting.
  $('#projects').stupidtable();
  $('#projects th').append('<span class="glyphicon asc-icon glyphicon-circle-arrow-down"></span>' +
    '<span class="glyphicon desc-icon glyphicon-circle-arrow-up"></span>');

  // Truncate abstracts.
  var truncate_length = 76;
  $('#projects .abstract').each(function() {
    var abs = $(this);
    var full_abstract = abs.text();

    if(full_abstract.length <= truncate_length)
      return;

    abs.data('full_abstract', full_abstract);
    truncate(abs, truncate_length);
  }).click(function() {
    var abs = $(this);
    if(abs.data('truncated')) {
      untruncate(abs, 'full_abstract');
    } else {
      truncate(abs, truncate_length);
    }
  });

  // Enable projects filter reset.
  $('#reset-projects-filter').click(function() {
    var form = $(this).parents('form');
    reset_form(form);
  });
});
