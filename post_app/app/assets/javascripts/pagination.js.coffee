jQuery ->
  if $('.apple_pagination').size() > 0
    $(window).on 'scroll', ->
      more_posts_url = $('.pagination .next_page a').attr('href')
      if more_posts_url && $(window).scrollTop() > $(document).height() - $(window).height() - 60
        $('.pagination').html('<img src="/assets/ajax-loader.gif" style="width: 60px; height: auto;" alt="Loading..." title="Loading..."/>')
        $.getScript more_posts_url
      return
  return