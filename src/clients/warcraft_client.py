import requests
from authlib.integrations.requests_client import OAuth2Session
from uplink import Consumer, Query, get, params, returns

from config.client_config import ClientConfiguration
from config.region_config import Locale, Region


class WarcraftClient(Consumer):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: Region = Region.us,
        locale: Locale = Locale.en_US,
        **kwargs,
    ):
        self.client_config = ClientConfiguration(
            client_id, client_secret, region, locale
        )
        client = self.get_client(**kwargs)
        super().__init__(base_url=self.client_config.host, client=client)
        self._inject(Query("locale").with_value(self.client_config.locale.name))

    def get_client(self, **kwargs):
        if "client" in kwargs.keys():
            return kwargs.get("client")
        else:
            oath_response = requests.get(
                f"{self.client_config.oauth_host}/oauth/.well-known/openid-configuration"
            ).json()
            token_endpoint = oath_response["token_endpoint"]
            client = OAuth2Session(
                self.client_config.client_id,
                self.client_config.client_secret,
                scope="openid",
                token_endpoint=token_endpoint,
                grant_type="client_credentials",
            )
            client.fetch_token()
            return client

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/achievement-category/index")
    def get_achievement_categories_index(self):
        """Returns an index of achievement categories."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/achievement-category/{achievementCategoryId}")
    def get_achievement_category(self, achievementCategoryId: int):
        """Returns an achievement category by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/achievement/index")
    def get_achievements_index(self):
        """Returns an index of achievements."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/achievement/{achievementId}")
    def get_achievement(self, achievementId: int):
        """Returns an achievement by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/achievement/{achievementId}")
    def get_achievement_media(self, achievementId: int):
        """Returns media for an achievement by ID."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/connected-realm/{connectedRealmId}/auctions")
    def get_auctions(self, connectedRealmId: int):
        """Returns all active auctions for a connected realm."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/azerite-essence/index")
    def get_azerite_essences_index(self):
        """Returns an index of azerite essences."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/azerite-essence/{azeriteEssenceId}")
    def get_azerite_essence(self, azeriteEssenceId: int):
        """Returns an azerite essence by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/azerite-essence/{azeriteEssenceId}")
    def get_azerite_essence_media(self, azeriteEssenceId: int):
        """Returns media for an azerite essence by ID."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/connected-realm/index")
    def get_connected_realms_index(self):
        """Returns an index of connected realms."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/connected-realm/{connectedRealmId}")
    def get_connected_realm(self, connectedRealmId: int):
        """Returns a connected realm by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/creature-family/index")
    def get_creature_families_index(self):
        """Returns an index of creature families."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/creature-family/{creatureFamilyId}")
    def get_creature_family(self, creatureFamilyId: int):
        """Returns a creature family by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/creature-type/index")
    def get_creature_types_index(self):
        """Returns an index of creature types."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/creature-type/{creatureTypeId}")
    def get_creature_type(self, creatureTypeId: int):
        """Returns a creature type by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/creature/{creatureId}")
    def get_creature(self, creatureId: int):
        """Returns a creature by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/creature-display/{creatureDisplayId}")
    def get_creature_display_media(self, creatureDisplayId: int):
        """Returns media for a creature display by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/creature-family/{creatureFamilyId}")
    def get_creature_family_media(self, creatureFamilyId: int):
        """Returns media for a creature family by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/guild-crest/index")
    def get_guild_crest_components_index(self):
        """Returns an index of guild crest media."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/guild-crest/border/{borderId}")
    def get_guild_crest_border_media(self, borderId: int):
        """Returns media for a guild crest border by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/guild-crest/emblem/{emblemId}")
    def get_guild_crest_emblem_media(self, emblemId: int):
        """Returns media for a guild crest emblem by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/item-class/index")
    def get_item_classes_index(self):
        """Returns an index of item classes."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/item-class/{itemClassId}")
    def get_item_class(self, itemClassId: int):
        """eturns an item class by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/item-set/index")
    def get_item_sets_index(self):
        """Returns an index of item sets."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/item-set/{itemSetId}")
    def get_item_set(self, itemSetId: int):
        """Returns an item set by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}")
    def get_item_subclass(self, itemClassId: int, itemSubclassId: int):
        """Returns an item subclass by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/item/{itemId}")
    def get_item(self, itemId: int):
        """Returns an item by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/item/{itemId}")
    def get_item_media(self, itemId: int):
        """Returns media for an item by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/journal-expansion/index")
    def get_journal_expansions_index(self):
        """Returns an index of journal expansions."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/journal-expansion/{journalExpansionId}")
    def get_journal_expansion(self, journalExpansionId: int):
        """Returns a journal expansion by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/journal-encounter/index")
    def get_journal_encounters_index(self):
        """Returns an index of journal encounters."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/journal-encounter/{journalEncounterId}")
    def get_journal_encounter(self, journalEncounterId: int):
        """Returns a journal encounter by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/journal-instance/index")
    def get_journal_instances_index(self):
        """Returns an index of journal instances."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/journal-instance/{journalInstanceId}")
    def get_journal_instance(self, journalInstanceId: int):
        """Returns a journal instance."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/journal-instance/{journalInstanceId}")
    def get_journal_instance_media(self, journalInstanceId: int):
        """Returns media for a journal instance by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/mount/index")
    def get_mount_index(self):
        """Returns an index of mounts."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/mount/{mountId}")
    def get_mount(self, mountId: int):
        """Returns a mount by ID."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/keystone-affix/index")
    def get_mythic_keystone_affixes_index(self):
        """Returns an index of mythic keystone affixes."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/keystone-affix/{keystoneAffixId}")
    def get_mythic_keystone_affix(self, keystoneAffixId: int):
        """Returns an index of mythic keystone affixes."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/media/keystone-affix/{keystoneAffixId}")
    def get_mythic_keystone_affix_media(self, keystoneAffixId: int):
        """Returns media for a mythic keystone affix by ID."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/dungeon/index")
    def get_mythic_keystone_dungeons_index(self):
        """Returns an index of Mythic Keystone dungeons."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/dungeon/{dungeonId}")
    def get_mythic_keystone_dungeon(self, dungeonId: int):
        """Returns a Mythic Keystone dungeon by ID."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/index")
    def get_mythic_keystone_index(self):
        """Returns an index of links to other documents related to Mythic Keystone dungeons."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/period/index")
    def get_mythic_keystone_periods_index(self):
        """Returns an index of Mythic Keystone periods."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/period/{periodId}")
    def get_mythic_keystone_period(self, periodId: int):
        """Returns a Mythic Keystone period by ID."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/season/index")
    def get_mythic_keystone_seasons_index(self):
        """Returns an index of Mythic Keystone seasons."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/mythic-keystone/season/{seasonId}")
    def get_mythic_keystone_season(self, seasonId: int):
        """Returns a Mythic Keystone season by ID."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index")
    def get_mythic_keystone_leaderboards_index(self, connectedRealmId: int):
        """Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get(
        "/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}"
    )
    def get_mythic_keystone_leaderboard(
        self, connectedRealmId: int, dungeonId: int, period: int
    ):
        """Returns a weekly Mythic Keystone Leaderboard by period."""

    @returns.json
    @params({"namespace": "dynamic-us"})
    @get("/data/wow/leaderboard/hall-of-fame/{raid}/{faction}")
    def get_mythic_raid_leaderboard(self, raid: str, faction: str):
        """Returns the leaderboard for a given raid and faction."""

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/pet/index")
    def get_pets_index(self):
        """Returns an index of battle pets."""

    @returns.json
    @params({"namespace": "static-us"})
    @get(" /data/wow/pet/{petId}")
    def get_pet(self, petId: int):
        """Returns a battle pets by ID."""
