// function SendCommendText() {
//     var comment = $('#commendText').val();
//
//     $.get('/articles/add-article-comment', {
//         articleComment: comment,
//         parentId: null,
//         articleId: 23
//     }).then(res => {
//         console.log(res);
//     });
// }


function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}