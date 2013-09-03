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

  // Set initial sort on year.
  $('#projects th').eq(1).click();

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
});
