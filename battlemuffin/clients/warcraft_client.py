import requests
from authlib.integrations.requests_client import OAuth2Session
from uplink import Consumer, Header, Query, get, returns

from battlemuffin.config.client_config import ClientConfiguration
from battlemuffin.config.region_config import Locale, Region
from battlemuffin.hooks.handlers import dynamic_locale, static_locale


class WarcraftClient(Consumer):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: Region = Region.us,
        locale: Locale = None,
        **kwargs,
    ):
        self.client_config = ClientConfiguration(
            client_id, client_secret, region, locale
        )
        client = self.get_client(**kwargs)
        super().__init__(base_url=self.client_config.host, client=client)

        if self.client_config.locale:
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
    @static_locale
    @get("/data/wow/achievement-category/index")
    def get_achievement_categories_index(self):
        """Returns an index of achievement categories."""

    @returns.json
    @static_locale
    @get("/data/wow/achievement-category/{achievementCategoryId}")
    def get_achievement_category(self, achievementCategoryId: int):
        """Returns an achievement category by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/achievement/index")
    def get_achievements_index(self):
        """Returns an index of achievements."""

    @returns.json
    @static_locale
    @get("/data/wow/achievement/{achievementId}")
    def get_achievement(self, achievementId: int):
        """Returns an achievement by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/achievement/{achievementId}")
    def get_achievement_media(self, achievementId: int):
        """Returns media for an achievement by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/connected-realm/{connectedRealmId}/auctions")
    def get_auctions(self, connectedRealmId: int):
        """Returns all active auctions for a connected realm."""

    @dynamic_locale
    @get("/data/wow/connected-realm/{connectedRealmId}/auctions")
    def get_auctions_raw_response(self, connectedRealmId: int):
        """Returns raw auctions response for a connected realm."""

    @dynamic_locale
    @get("/data/wow/connected-realm/{connectedRealmId}/auctions")
    def get_auctions_if_modified_since(
        self, connectedRealmId: int, if_modified_since: Header("If-Modified-Since")
    ):
        """Returns all active auctions for a connected realm if modified since given date."""

    @returns.json
    @static_locale
    @get("/data/wow/azerite-essence/index")
    def get_azerite_essences_index(self):
        """Returns an index of azerite essences."""

    @returns.json
    @static_locale
    @get("/data/wow/azerite-essence/{azeriteEssenceId}")
    def get_azerite_essence(self, azeriteEssenceId: int):
        """Returns an azerite essence by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/azerite-essence/{azeriteEssenceId}")
    def get_azerite_essence_media(self, azeriteEssenceId: int):
        """Returns media for an azerite essence by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/connected-realm/index")
    def get_connected_realms_index(self):
        """Returns an index of connected realms."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/connected-realm/{connectedRealmId}")
    def get_connected_realm(self, connectedRealmId: int):
        """Returns a connected realm by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/creature-family/index")
    def get_creature_families_index(self):
        """Returns an index of creature families."""

    @returns.json
    @static_locale
    @get("/data/wow/creature-family/{creatureFamilyId}")
    def get_creature_family(self, creatureFamilyId: int):
        """Returns a creature family by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/creature-type/index")
    def get_creature_types_index(self):
        """Returns an index of creature types."""

    @returns.json
    @static_locale
    @get("/data/wow/creature-type/{creatureTypeId}")
    def get_creature_type(self, creatureTypeId: int):
        """Returns a creature type by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/creature/{creatureId}")
    def get_creature(self, creatureId: int):
        """Returns a creature by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/creature-display/{creatureDisplayId}")
    def get_creature_display_media(self, creatureDisplayId: int):
        """Returns media for a creature display by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/creature-family/{creatureFamilyId}")
    def get_creature_family_media(self, creatureFamilyId: int):
        """Returns media for a creature family by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/guild-crest/index")
    def get_guild_crest_components_index(self):
        """Returns an index of guild crest media."""

    @returns.json
    @static_locale
    @get("/data/wow/media/guild-crest/border/{borderId}")
    def get_guild_crest_border_media(self, borderId: int):
        """Returns media for a guild crest border by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/guild-crest/emblem/{emblemId}")
    def get_guild_crest_emblem_media(self, emblemId: int):
        """Returns media for a guild crest emblem by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/item-class/index")
    def get_item_classes_index(self):
        """Returns an index of item classes."""

    @returns.json
    @static_locale
    @get("/data/wow/item-class/{itemClassId}")
    def get_item_class(self, itemClassId: int):
        """eturns an item class by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/item-set/index")
    def get_item_sets_index(self):
        """Returns an index of item sets."""

    @returns.json
    @static_locale
    @get("/data/wow/item-set/{itemSetId}")
    def get_item_set(self, itemSetId: int):
        """Returns an item set by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}")
    def get_item_subclass(self, itemClassId: int, itemSubclassId: int):
        """Returns an item subclass by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/item/{itemId}")
    def get_item(self, itemId: int):
        """Returns an item by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/item/{itemId}")
    def get_item_media(self, itemId: int):
        """Returns media for an item by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/journal-expansion/index")
    def get_journal_expansions_index(self):
        """Returns an index of journal expansions."""

    @returns.json
    @static_locale
    @get("/data/wow/journal-expansion/{journalExpansionId}")
    def get_journal_expansion(self, journalExpansionId: int):
        """Returns a journal expansion by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/journal-encounter/index")
    def get_journal_encounters_index(self):
        """Returns an index of journal encounters."""

    @returns.json
    @static_locale
    @get("/data/wow/journal-encounter/{journalEncounterId}")
    def get_journal_encounter(self, journalEncounterId: int):
        """Returns a journal encounter by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/journal-instance/index")
    def get_journal_instances_index(self):
        """Returns an index of journal instances."""

    @returns.json
    @static_locale
    @get("/data/wow/journal-instance/{journalInstanceId}")
    def get_journal_instance(self, journalInstanceId: int):
        """Returns a journal instance."""

    @returns.json
    @static_locale
    @get("/data/wow/media/journal-instance/{journalInstanceId}")
    def get_journal_instance_media(self, journalInstanceId: int):
        """Returns media for a journal instance by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/mount/index")
    def get_mount_index(self):
        """Returns an index of mounts."""

    @returns.json
    @static_locale
    @get("/data/wow/mount/{mountId}")
    def get_mount(self, mountId: int):
        """Returns a mount by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/keystone-affix/index")
    def get_mythic_keystone_affixes_index(self):
        """Returns an index of mythic keystone affixes."""

    @returns.json
    @static_locale
    @get("/data/wow/keystone-affix/{keystoneAffixId}")
    def get_mythic_keystone_affix(self, keystoneAffixId: int):
        """Returns an index of mythic keystone affixes."""

    @returns.json
    @static_locale
    @get("/data/wow/media/keystone-affix/{keystoneAffixId}")
    def get_mythic_keystone_affix_media(self, keystoneAffixId: int):
        """Returns media for a mythic keystone affix by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/dungeon/index")
    def get_mythic_keystone_dungeons_index(self):
        """Returns an index of Mythic Keystone dungeons."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/dungeon/{dungeonId}")
    def get_mythic_keystone_dungeon(self, dungeonId: int):
        """Returns a Mythic Keystone dungeon by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/index")
    def get_mythic_keystone_index(self):
        """Returns an index of links to other documents related to Mythic Keystone dungeons."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/period/index")
    def get_mythic_keystone_periods_index(self):
        """Returns an index of Mythic Keystone periods."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/period/{periodId}")
    def get_mythic_keystone_period(self, periodId: int):
        """Returns a Mythic Keystone period by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/season/index")
    def get_mythic_keystone_seasons_index(self):
        """Returns an index of Mythic Keystone seasons."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/mythic-keystone/season/{seasonId}")
    def get_mythic_keystone_season(self, seasonId: int):
        """Returns a Mythic Keystone season by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index")
    def get_mythic_keystone_leaderboards_index(self, connectedRealmId: int):
        """Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm."""

    @returns.json
    @dynamic_locale
    @get(
        "/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}"
    )
    def get_mythic_keystone_leaderboard(
        self, connectedRealmId: int, dungeonId: int, period: int
    ):
        """Returns a weekly Mythic Keystone Leaderboard by period."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/leaderboard/hall-of-fame/{raid}/{faction}")
    def get_mythic_raid_leaderboard(self, raid: str, faction: str):
        """Returns the leaderboard for a given raid and faction."""

    @returns.json
    @static_locale
    @get("/data/wow/pet/index")
    def get_pets_index(self):
        """Returns an index of battle pets."""

    @returns.json
    @static_locale
    @get("/data/wow/pet/{petId}")
    def get_pet(self, petId: int):
        """Returns a battle pets by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-class/index")
    def get_playable_classes_index(self):
        """Returns an index of playable classes."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-class/{classId}")
    def get_playable_class(self, classId: int):
        """Returns a playable class by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/playable-class/{playableClassId}")
    def get_playable_class_media(self, playableClassId: int):
        """Returns media for a playable class by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-class/{classId}/pvp-talent-slots")
    def get_pvp_talent_slots(self, classId: int):
        """Returns the PvP talent slots for a playable class by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-race/index")
    def get_playable_races_index(self):
        """Returns an index of playable races."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-race/{playableRaceId}")
    def get_playable_race(self, playableRaceId: int):
        """Returns a playable race by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-specialization/index")
    def get_playable_specializations_index(self):
        """Returns an index of playable specializations."""

    @returns.json
    @static_locale
    @get("/data/wow/playable-specialization/{specId}")
    def get_playable_specialization(self, specId: int):
        """Returns a playable specialization by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/playable-specialization/{specId}")
    def get_playable_specialization_media(self, specId: int):
        """Returns media for a playable specialization by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/power-type/index")
    def get_power_types_index(self):
        """Returns an index of power types."""

    @returns.json
    @static_locale
    @get("/data/wow/power-type/{powerTypeId}")
    def get_power_type(self, powerTypeId: int):
        """Returns a power type by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/profession/index")
    def get_professions_index(self):
        """Returns an index of professions."""

    @returns.json
    @static_locale
    @get("/data/wow/profession/{professionId}")
    def get_profession(self, professionId: int):
        """Returns a profession by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/profession/{professionId}")
    def get_profession_media(self, professionId: int):
        """Returns media for a profession by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/profession/{professionId}/skill-tier/{skillTierId}")
    def get_profession_skill_tier(self, professionId: int, skillTierId: int):
        """Returns a skill tier for a profession by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/recipe/{recipeId}")
    def get_recipe(self, recipeId: int):
        """Returns a recipe by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/recipe/{recipeId}")
    def get_recipe_media(self, recipeId: int):
        """Returns media for a recipe by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/pvp-season/index")
    def get_pvp_seasons_index(self):
        """Returns an index of PvP seasons."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/pvp-season/{pvpSeasonId}")
    def get_pvp_season(self, pvpSeasonId: int):
        """Returns a PvP season by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/index")
    def get_pvp_leaderboards_index(self, pvpSeasonId: int):
        """Returns an index of PvP leaderboards for a PvP season."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/{pvpBracket}")
    def get_pvp_leaderboard(self, pvpSeasonId: int, pvpBracket: str):
        """Returns the PvP leaderboard of a specific PvP bracket for a PvP season."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/pvp-season/{pvpSeasonId}/pvp-reward/index")
    def get_pvp_rewards_index(self, pvpSeasonId: int):
        """Returns an index of PvP rewards for a PvP season."""

    @returns.json
    @static_locale
    @get("/data/wow/pvp-tier/index")
    def get_pvp_tiers_index(self):
        """Returns an index of PvP tiers."""

    @returns.json
    @static_locale
    @get("/data/wow/pvp-tier/{pvpTierId}")
    def get_pvp_tier(self, pvpTierId: int):
        """Returns a PvP tier by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/pvp-tier/{pvpTierId}")
    def get_pvp_tier_media(self, pvpTierId: int):
        """Returns media for a PvP tier by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/index")
    def get_quests_index(self):
        """Returns an index of quests."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/{questId}")
    def get_quest(self, questId: int):
        """Returns a quest by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/category/index")
    def get_quest_categories_index(self):
        """Returns an index of quest categories (such as quests for a specific class, profession, or storyline)."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/category/{questCategoryId}")
    def get_quest_category(self, questCategoryId: int):
        """Returns a quest category by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/area/index")
    def get_quest_areas_index(self):
        """Returns an index of quest areas."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/area/{questAreaId}")
    def get_quest_area(self, questAreaId: int):
        """Returns a quest area by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/type/index")
    def get_quest_types_index(self):
        """Returns an index of quest types (such as PvP quests, raid quests, or account quests)."""

    @returns.json
    @static_locale
    @get("/data/wow/quest/type/{questTypeId}")
    def get_quest_type(self, questTypeId: int):
        """Returns a quest type by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/realm/index")
    def get_realms_index(self):
        """Returns an index of realms."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/realm/{realmSlug}")
    def get_realm(self, realmSlug: str):
        """Returns a single realm by slug."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/region/index")
    def get_regions_index(self):
        """Returns an index of regions."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/region/{regionId}")
    def get_region(self, regionId: int):
        """Returns a region by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/reputation-faction/index")
    def get_reputation_factions_index(self):
        """Returns an index of reputation factions."""

    @returns.json
    @static_locale
    @get("/data/wow/reputation-faction/{reputationFactionId}")
    def get_reputation_faction(self, reputationFactionId: int):
        """Returns a single reputation faction by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/reputation-tiers/index")
    def get_reputation_tiers_index(self):
        """Returns an index of reputation tiers."""

    @returns.json
    @static_locale
    @get("/data/wow/reputation-tiers/{reputationTiersId}")
    def get_reputation_tiers(self, reputationTiersId: int):
        """Returns a single set of reputation tiers by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/spell/{spellId}")
    def get_spell(self, spellId: int):
        """Returns a spell by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/media/spell/{spellId}")
    def get_spell_media(self, spellId: int):
        """Returns media for a spell by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/talent/index")
    def get_talents_index(self):
        """Returns an index of talents."""

    @returns.json
    @static_locale
    @get("/data/wow/talent/{talentId}")
    def get_talent(self, talentId: int):
        """Returns a talent by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/pvp-talent/index")
    def get_pvp_talents_index(self):
        """Returns an index of PvP talents."""

    @returns.json
    @static_locale
    @get("/data/wow/pvp-talent/{pvpTalentId}")
    def get_pvp_talent(self, pvpTalentId: int):
        """Returns a PvP talent by ID."""

    @returns.json
    @static_locale
    @get("/data/wow/title/index")
    def get_titles_index(self):
        """Returns an index of titles."""

    @returns.json
    @static_locale
    @get("/data/wow/title/{titleId}")
    def get_title(self, titleId: int):
        """Returns a title by ID."""

    @returns.json
    @dynamic_locale
    @get("/data/wow/token/index")
    def get_wow_token_index(self):
        """Returns an index of titles."""
