// globals

window.$IDX = null;

$(function ()
{
    $('#sarchbox').hide();
    $.ajax({
        url: '/data.json'
    }).done(function (data)
    {
        console.log(data);
        window.$IDX = lunr(function ()
        {
            this.field('title');
            this.field('subtitle');
            this.field('summary');
            this.field('date');

            for (let i = 0; i < data.length; i++)
            {
                this.add(
                {
                    'id': data[i]['slug'],
                    'title': data[i]['title'],
                    'subtitle': data[i]['subtitle'],
                    'date': data[i]['date'],
                    'tags': data[i]['tags'],
                    'summary': data[i]['summary'],
                    'slug': data[i]['slug']
                });
            }
        });
        $('#sarchbox').show();
    });

    $(document).off('click', '#btn_search');
    $(document).on('click', '#btn_search', function(evt)
    {
        evt.stopPropagation();
        evt.preventDefault();
        const value = $('#text').val();
        const results = window.$IDX.search($.trim(value));
        let visibles_slugs = [];
        for(let i=0; i<results.length; i++)
        {
            visibles_slugs.push(results[i].ref);
        }
        $('article').hide();
        $('article').each(function(i,v)
        {
            const slug = $(v).attr('data-slug');
            if(visibles_slugs.indexOf(slug) > -1)
            {
                $(v).show();
            }
        });
        
    });

    $(document).off('click', '#btn_reset');
    $(document).on('click', '#btn_reset', function(evt)
    {
        evt.stopPropagation();
        evt.preventDefault();
        $('#text').val('');
    });
});