let searchForm=document.getElementById('searchForm')
let page_links=document.getElementsByClassName('page-link')


    if (searchForm){
        for (let i=0; i<page_links.length;i++){
            page_links[i].addEventListener('click',function (e){
                e.preventDefault()

                let page=this.dataset.page
                console.log(page)

                searchForm.innerHTML+=`<input value=${page} name="page" hidden/>`

                searchForm.submit()


            })
        }

    }