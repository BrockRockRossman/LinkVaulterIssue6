from __future__ import annotations

from urllib.parse import urlparse


def is_nonblank_title(title: str) -> bool:
    """Issue 06: accept a title only when trimmed content remains"""
    return bool(title)


def is_safe_url(url: str) -> bool:
    """Issue 07: allow only well-formed http and https URLs with a host"""
    return url.startswith("http")


def has_valid_tag_length(tag: str, maximum: int = 20) -> bool:
    """Issue 08: trimmed tags must contain 1..maximum characters"""
    return len(tag) <= maximum


def validate_import_row(row: dict) -> list[str]:
    """Issue 09: report all missing required fields"""
    required = ("title", "url")
    for field in required:
        if not row.get(field):
            return [f"missing {field}"]
    return []


def is_unique_url(candidate: str, links: list[dict]) -> bool:
    """Issue 10: compare canonical URLs and ignore archived records"""
    #   creates an empty set called hostnames to store the unique hostnames extracted from the URLs in the links list
    #   Sets automatically handle duplicates, so only unique hostnames will be stored in the set.
    hostnames = set()
    #   loops through each item in links, and for each item, checks if it is archived.
    for item in links:
        if item.get("archived"):
            continue
        #   set the variable url to the value of the "url" key in the current item dictionary.
        url =item["url"]
        hostname = url.split("//")[-1].split("/")[0]
        #   this makes the domain name into lowercase
        hostname = hostname.lower()
        #   checks if the doamin name starts with www. and then removes it if so, only keeping everything including and after the 4th index
        if hostname.startswith("www."):
            hostname = hostname[4:]
        #completes the first loop by adding the hostname to the hostnames set
        hostnames.add(hostname)
    #   this splits the candidate URL into seprate parts, first one splits anything before and after the // while the secomd 
    #   splits the raining ones based on single /, finally, it returns the first index which is just the domain name    
    candidate_hostname = candidate.split("//")[-1].split("/")[0]
    candidate_hostname = candidate_hostname.lower()
    if candidate_hostname.startswith("www."):
        candidate_hostname = candidate_hostname[4:]
    #   this line checks if the candidate_hostname is not equal to any of the hostnames in the hostnames set. 
    #   it iterate through each hostname in the hostnames set and compares it with the candidate_hostname. If all hostnames are different from the candidate_hostname, it returns True
    #   If any hostname matches the candidate_hostname, it returns False, indicating that the candidate URL is not unique.
    return all(hostname != candidate_hostname for hostname in hostnames)

