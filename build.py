#index
top_template = open('templates/top.html').read()
body = open('content/index.html').read()
bottom_template = open('templates/bottom.html').read()
index_html = top_template + body + bottom_template 
open('docs/index.html', 'w+').write(index_html)

#testimonial 
content = open('content/testimonials.html').read()
testimonials = top_template + content + bottom_template
open('docs/testimonials.html', 'w+').write(testimonials) 



#blog 
page = open('content/blog.html').read()
blog = top_template + page + bottom_template
open('docs/blog.html', 'w+').write(blog) 


#blog
page = open('content/blog.html').read()
blog = top_template + page + bottom_template
open('docs/blog.html', 'w+').write(blog) 

#blog
#testimonial 
page = open('content/blog.html').read()
blog = top_template + page + bottom_template
open('docs/blog.html', 'w+').write(blog) 

