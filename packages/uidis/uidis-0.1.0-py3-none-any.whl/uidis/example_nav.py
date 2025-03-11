from .scopes import scope, item
from .shorts import icons

Dashboard = scope(
    "Dashboard",
    (
        item("Notifications", "/ongoing"),
        item("Ongoing Tasks", "/ongoing"),
        item("Completed Tasks", "/completed"),
    ),
)

RapidScans = scope(
    "Scans",
    (
        item("Ad-hoc", "/scan/adhoc", icons.radar),
        item("False Positive", "/scan/false-positive", icons.block),
        item("History", "/scan/history", icons.history),
    ),
    icons.radar,
)

RapidIPAM = scope(
    "IPAM",
    (
        item("Import", "/ipam/import", icons.download),
        item("Fill Missing Details", "/ipam/fill", icons.edit),
        item("Review", "/ipam/review", icons.mystery),
        item("Push to Rapid7", "/ipam/push", icons.cloud_upload),
    ),
    icons.dns,
)

RapidOther = scope(
    "Other",
    (
        item("Tags", "/tags", icons.label),
        item("Groups", "/groups", icons.group),
        item("Environment Check", "/env-check", icons.problem),
        item("Digital Workplace", "/workplace", icons.browser_updated),
    ),
    icons.more,
)

RapidUsers = scope(
    "Users",
    (
        item("Create", "/users/create", icons.group_add),
        item("Copy Groups", "/users/copy", icons.file_copy),
        item("Add Groups", "/users/add", icons.playlist_add),
    ),
    icons.person,
)


Rapid = scope(
    "Rapid7",
    (
        item("Search", "/search", icons.search),
        RapidScans,
        RapidUsers,
        RapidIPAM,
        RapidOther,
    ),
    icons.pets,
)

Apps = scope(
    "Apps",
    (Dashboard, Rapid),
    icons.apps,
)
