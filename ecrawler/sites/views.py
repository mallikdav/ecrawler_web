from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import transaction
from forms import *
from crawler import Crawler
from links.models import Links

def home(request):
    template = loader.get_template('home.html')
    contextDict = {
        'form': Site,
    }
    if request.method == 'POST':
        if 'site' in request.POST:
            pending_sites = [request.POST['site']]
            look_up = "a"
            while 1==1:
                if len(pending_sites) != 0:
                    site_to_crawl = pending_sites.pop(0)
                    print site_to_crawl
                    if site_to_crawl[-1] != '/':
                        site_to_crawl = site_to_crawl+"/"
                    crawler = Crawler(site_to_crawl, look_up)
                    crawled_items = crawler.crawl()
                    if 'result' in crawled_items:
                        site = Sites.objects.filter(site=site_to_crawl)
                        if not site:
                            site = Sites()
                        else:
                            site = site[0]
                        site.site = site_to_crawl
                        site.active_or_dead = True
                        site.save()
                        for anchor in crawled_items['result']:
                            if not ("https://" in anchor or "http://" in anchor):
                                anchor = site_to_crawl + anchor.replace("../", "")
                                # crawler = Crawler(anchor, look_up)
                                # test_output = crawler.test_site_to_crawl()
                                # if test_output == "Success":
                                # anchorList.append(anchor)
                            pending_sites.append(anchor)
                            link = Links.objects.filter(url=anchor, parentSite=site)
                            if not link:
                                link = Links()
                                link.url = anchor
                                link.parentSite = site
                                link.save()
            else:
                contextDict['error'] = crawled_items['error']
    contextDict['old_site'] = getOldEntries()
    context = RequestContext(request, contextDict)
    return HttpResponse(template.render(context))

def getOldEntries():
    old_sites = []
    for site in Sites.objects.all().order_by('-added'):
        site.child = Links.objects.filter(parentSite = site)
        old_sites.append(site)
    return old_sites