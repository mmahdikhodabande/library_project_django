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


/*
function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}


function AddProductToOrder(productId) {
    const productCount = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        if (res.status === 'success') {
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: res.confirmButtonText
            });
        } else if (res.status === 'not_found') {
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: res.confirmButtonText
            });
        } else if (res.status === 'not_auth') {
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: res.confirmButtonText
            });
        }
    });
}

function RemoveOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res => {
        console.log(res);
        // if (res.status === 'success'){
        //     $('#order-detail-content').html(res.body);
        // }
    });
}


function ChangeOrderDetailCount(detailId, state){
    // console.log(detailId, state);
    $.get('/user/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}*/
