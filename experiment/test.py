import r7ivm3


###################################

# r7 = r7ivm3.ClientForHumans(config_file_path="config.ini", disable_insecure_request_warnings=True)
#
# blob = r7.get_all.site_api.get_sites(size=4, view="summary")

r7 = r7ivm3.ClientForHumans(config_file_path="config.ini", disable_insecure_request_warnings=True)

test = r7ivm3.get_all_pages(r7.site_api.get_sites, size=3, view="summary")

for r in test["resources"]:
    print(r["id"])

    # (r7.site_api.get_sites(size=4, view="summary"))

# print(blob.links)
# sites = r7.site_api.get_sites(size=4, view="summary")
#
# site_dict = sites.to_dict()
#
# print(site_dict["links"])
#
# for link in site_dict["links"]:
#     if link["rel"] == "next":
#         print(link["href"])
# #print(sites.page.total_pages)



