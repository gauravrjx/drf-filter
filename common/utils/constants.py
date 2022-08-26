(ALL, PENDING, APPROVED, DENIED, DRAFT,
 PUBLISHED) = (
    'All', 
    'Pending', 
    'Approved',
    'Denied', 
    'Draft', 
    'Published',
)

BLOG_STATUS_CHOICES = (
    (DRAFT, 'Draft'),
    (PENDING, 'Pending'),
    (DENIED, 'Denied'),
    (PUBLISHED, 'Published')
)

CATEGORIES_CHOICES =  [
    'Politics', 'Sports', 'IT', 'Health', 'Finance', 'Entertainment', 
    'Education', 'Business', 'Random'
]

BLOG_STATUS_CHOICES_FOR_FACTORY = ['DRAFT', 'PENDING', 'DENIED', 'PUBLISHED']