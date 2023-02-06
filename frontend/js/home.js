const ProductContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

ProductContainers.forEach((item, i) => {
    let ContainerDimensions = item.getBoundingClientRect();
    let ContainerWidth = ContainerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += ContainerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= ContainerWidth;
    })
})