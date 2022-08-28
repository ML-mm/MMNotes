$(document).ready(function () {
    jQuery(function ($) {
        let $list = $('.note-list');
        $list.jscroll({
            loadingHtml: '<div class="text-center">' + '<img src="/static/media/299.gif"' + ' alt="Loading" /> </div>',
            padding: 100,
            pagingSelector: '.pagination',
            nextSelector: 'a.next-page:last',
            contentSelector: '.card,.pagination'
        });
    });
});