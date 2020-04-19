import requests
from authlib.integrations.requests_client import OAuth2Session

from config.client_config import ClientConfiguration
from config.region_config import Locale, Region


class WarcraftClient:
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
        self.client = self.get_client(**kwargs)

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

    def get_achievement_categories_index(self):
        """Returns an index of achievement categories."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/achievement-category/index",
            params=self.client_config.static_params,
        ).json()

    def get_achievement_category(self, achievementCategoryId: int):
        """Returns an achievement category by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/achievement-category/{achievementCategoryId}",
            params=self.client_config.static_params,
        ).json()

    def get_achievements_index(self):
        """Returns an index of achievements."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/achievement/index",
            params=self.client_config.static_params,
        ).json()

    def get_achievement(self, achievementId: int):
        """Returns an achievement by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/achievement/{achievementId}",
            params=self.client_config.static_params,
        ).json()

    def get_achievement_media(self, achievementId: int):
        """Returns media for an achievement by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/achievement/{achievementId}",
            params=self.client_config.static_params,
        ).json()

    def get_auctions(self, connectedRealmId: int):
        """Returns all active auctions for a connected realm."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/connected-realm/{connectedRealmId}/auctions",
            params=self.client_config.dynamic_params,
        ).json()

    def get_azerite_essences_index(self):
        """Returns an index of azerite essences."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/azerite-essence/index",
            params=self.client_config.static_params,
        ).json()

    def get_azerite_essence(self, azeriteEssenceId: int):
        """Returns an azerite essence by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/azerite-essence/{azeriteEssenceId}",
            params=self.client_config.static_params,
        ).json()

    def get_azerite_essence_media(self, azeriteEssenceId: int):
        """Returns media for an azerite essence by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/azerite-essence/{azeriteEssenceId}",
            params=self.client_config.static_params,
        ).json()

    def get_connected_realms_index(self):
        """Returns an index of connected realms."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/connected-realm/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_connected_realm(self, connectedRealmId: int):
        """Returns a connected realm by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/connected-realm/{connectedRealmId}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_creature_families_index(self):
        """Returns an index of creature families."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/creature-family/index",
            params=self.client_config.static_params,
        ).json()

    def get_creature_family(self, creatureFamilyId: int):
        """Returns a creature family by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/creature-family/{creatureFamilyId}",
            params=self.client_config.static_params,
        ).json()

    def get_creature_types_index(self):
        """Returns an index of creature types."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/creature-type/index",
            params=self.client_config.static_params,
        ).json()

    def get_creature_type(self, creatureTypeId: int):
        """Returns a creature type by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/creature-type/{creatureTypeId}",
            params=self.client_config.static_params,
        ).json()

    def get_creature(self, creatureId: int):
        """Returns a creature by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/creature/{creatureId}",
            params=self.client_config.static_params,
        ).json()

    def get_creature_display_media(self, creatureDisplayId: int):
        """Returns media for a creature display by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/creature-display/{creatureDisplayId}",
            params=self.client_config.static_params,
        ).json()

    def get_creature_family_media(self, creatureFamilyId: int):
        """Returns media for a creature family by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/creature-family/{creatureFamilyId}",
            params=self.client_config.static_params,
        ).json()

    def get_guild_crest_components_index(self):
        """Returns an index of guild crest media."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/guild-crest/index",
            params=self.client_config.static_params,
        ).json()

    def get_guild_crest_border_media(self, borderId: int):
        """Returns media for a guild crest border by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/guild-crest/border/{borderId}",
            params=self.client_config.static_params,
        ).json()

    def get_guild_crest_emblem_media(self, emblemId: int):
        """Returns media for a guild crest emblem by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/guild-crest/emblem/{emblemId}",
            params=self.client_config.static_params,
        ).json()

    def get_item_classes_index(self):
        """Returns an index of item classes."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/item-class/index",
            params=self.client_config.static_params,
        ).json()

    def get_item_class(self, itemClassId: int):
        """eturns an item class by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/item-class/{itemClassId}",
            params=self.client_config.static_params,
        ).json()

    def get_item_sets_index(self):
        """Returns an index of item sets."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/item-set/index",
            params=self.client_config.static_params,
        ).json()

    def get_item_set(self, itemSetId: int):
        """Returns an item set by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/item-set/{itemSetId}",
            params=self.client_config.static_params,
        ).json()

    def get_item_subclass(self, itemClassId: int, itemSubclassId: int):
        """Returns an item subclass by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}",
            params=self.client_config.static_params,
        ).json()

    def get_item(self, itemId: int):
        """Returns an item by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/item/{itemId}",
            params=self.client_config.static_params,
        ).json()

    def get_item_media(self, itemId: int):
        """Returns media for an item by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/item/{itemId}",
            params=self.client_config.static_params,
        ).json()

    def get_journal_expansions_index(self):
        """Returns an index of journal expansions."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/journal-expansion/index",
            params=self.client_config.static_params,
        ).json()

    def get_journal_expansion(self, journalExpansionId: int):
        """Returns a journal expansion by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/journal-expansion/{journalExpansionId}",
            params=self.client_config.static_params,
        ).json()

    def get_journal_encounters_index(self):
        """Returns an index of journal encounters."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/journal-encounter/index",
            params=self.client_config.static_params,
        ).json()

    def get_journal_encounter(self, journalEncounterId: int):
        """Returns a journal encounter by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/journal-encounter/{journalEncounterId}",
            params=self.client_config.static_params,
        ).json()

    def get_journal_instances_index(self):
        """Returns an index of journal instances."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/journal-instance/index",
            params=self.client_config.static_params,
        ).json()

    def get_journal_instance(self, journalInstanceId: int):
        """Returns a journal instance."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/journal-instance/{journalInstanceId}",
            params=self.client_config.static_params,
        ).json()

    def get_journal_instance_media(self, journalInstanceId: int):
        """Returns media for a journal instance by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/journal-instance/{journalInstanceId}",
            params=self.client_config.static_params,
        ).json()

    def get_mount_index(self):
        """Returns an index of mounts."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mount/index",
            params=self.client_config.static_params,
        ).json()

    def get_mount(self, mountId: int):
        """Returns a mount by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mount/{mountId}",
            params=self.client_config.static_params,
        ).json()

    def get_mythic_keystone_affixes_index(self):
        """Returns an index of mythic keystone affixes."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/keystone-affix/index",
            params=self.client_config.static_params,
        ).json()

    def get_mythic_keystone_affix(self, keystoneAffixId: int):
        """Returns an index of mythic keystone affixes."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/keystone-affix/{keystoneAffixId}",
            params=self.client_config.static_params,
        ).json()

    def get_mythic_keystone_affix_media(self, keystoneAffixId: int):
        """Returns media for a mythic keystone affix by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/keystone-affix/{keystoneAffixId}",
            params=self.client_config.static_params,
        ).json()

    def get_mythic_keystone_dungeons_index(self):
        """Returns an index of Mythic Keystone dungeons."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/dungeon/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_dungeon(self, dungeonId: int):
        """Returns a Mythic Keystone dungeon by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/dungeon/{dungeonId}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_index(self):
        """Returns an index of links to other documents related to Mythic Keystone dungeons."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_periods_index(self):
        """Returns an index of Mythic Keystone periods."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/period/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_period(self, periodId: int):
        """Returns a Mythic Keystone period by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/period/{periodId}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_seasons_index(self):
        """Returns an index of Mythic Keystone seasons."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/season/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_season(self, seasonId: int):
        """Returns a Mythic Keystone season by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/mythic-keystone/season/{seasonId}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_leaderboards_index(self, connectedRealmId: int):
        """Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_keystone_leaderboard(
        self, connectedRealmId: int, dungeonId: int, period: int
    ):
        """Returns a weekly Mythic Keystone Leaderboard by period."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_mythic_raid_leaderboard(self, raid: str, faction: str):
        """Returns the leaderboard for a given raid and faction."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/leaderboard/hall-of-fame/{raid}/{faction}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_pets_index(self):
        """Returns an index of battle pets."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pet/index",
            params=self.client_config.static_params,
        ).json()

    def get_pet(self, petId: int):
        """Returns a battle pets by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pet/{petId}",
            params=self.client_config.static_params,
        ).json()

    def get_playable_classes_index(self):
        """Returns an index of playable classes."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-class/index",
            params=self.client_config.static_params,
        ).json()

    def get_playable_class(self, classId: int):
        """Returns a playable class by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-class/{classId}",
            params=self.client_config.static_params,
        ).json()

    def get_playable_class_media(self, playableClassId: int):
        """Returns media for a playable class by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/playable-class/{playableClassId}",
            params=self.client_config.static_params,
        ).json()

    def get_pvp_talent_slots(self, classId: int):
        """Returns the PvP talent slots for a playable class by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-class/{classId}/pvp-talent-slots",
            params=self.client_config.static_params,
        ).json()

    def get_playable_races_index(self):
        """Returns an index of playable races."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-race/index",
            params=self.client_config.static_params,
        ).json()

    def get_playable_race(self, playableRaceId: int):
        """Returns a playable race by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-race/{playableRaceId}",
            params=self.client_config.static_params,
        ).json()

    def get_playable_specializations_index(self):
        """Returns an index of playable specializations."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-specialization/index",
            params=self.client_config.static_params,
        ).json()

    def get_playable_specialization(self, specId: int):
        """Returns a playable specialization by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/playable-specialization/{specId}",
            params=self.client_config.static_params,
        ).json()

    def get_playable_specialization_media(self, specId: int):
        """Returns media for a playable specialization by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/playable-specialization/{specId}",
            params=self.client_config.static_params,
        ).json()

    def get_power_types_index(self):
        """Returns an index of power types."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/power-type/index",
            params=self.client_config.static_params,
        ).json()

    def get_power_type(self, powerTypeId: int):
        """Returns a power type by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/power-type/{powerTypeId}",
            params=self.client_config.static_params,
        ).json()

    def get_professions_index(self):
        """Returns an index of professions."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/profession/index",
            params=self.client_config.static_params,
        ).json()

    def get_profession(self, professionId: int):
        """Returns a profession by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/profession/{professionId}",
            params=self.client_config.static_params,
        ).json()

    def get_profession_media(self, professionId: int):
        """Returns media for a profession by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/profession/{professionId}",
            params=self.client_config.static_params,
        ).json()

    def get_profession_skill_tier(self, professionId: int, skillTierId: int):
        """Returns a skill tier for a profession by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/profession/{professionId}/skill-tier/{skillTierId}",
            params=self.client_config.static_params,
        ).json()

    def get_recipe(self, recipeId: int):
        """Returns a recipe by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/recipe/{recipeId}",
            params=self.client_config.static_params,
        ).json()

    def get_recipe_media(self, recipeId: int):
        """Returns media for a recipe by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/recipe/{recipeId}",
            params=self.client_config.static_params,
        ).json()

    def get_pvp_seasons_index(self):
        """Returns an index of PvP seasons."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-season/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_pvp_season(self, pvpSeasonId: int):
        """Returns a PvP season by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-season/{pvpSeasonId}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_pvp_leaderboards_index(self, pvpSeasonId: int):
        """Returns an index of PvP leaderboards for a PvP season."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_pvp_leaderboard(self, pvpSeasonId: int, pvpBracket: str):
        """Returns the PvP leaderboard of a specific PvP bracket for a PvP season."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/{pvpBracket}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_pvp_rewards_index(self, pvpSeasonId: int):
        """Returns an index of PvP rewards for a PvP season."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-season/{pvpSeasonId}/pvp-reward/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_pvp_tiers_index(self):
        """Returns an index of PvP tiers."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-tier/index",
            params=self.client_config.static_params,
        ).json()

    def get_pvp_tier(self, pvpTierId: int):
        """Returns a PvP tier by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-tier/{pvpTierId}",
            params=self.client_config.static_params,
        ).json()

    def get_pvp_tier_media(self, pvpTierId: int):
        """Returns media for a PvP tier by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/pvp-tier/{pvpTierId}",
            params=self.client_config.static_params,
        ).json()

    def get_quests_index(self):
        """Returns an index of quests."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/index",
            params=self.client_config.static_params,
        ).json()

    def get_quest(self, questId: int):
        """Returns a quest by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/{questId}",
            params=self.client_config.static_params,
        ).json()

    def get_quest_categories_index(self):
        """Returns an index of quest categories (such as quests for a specific class, profession, or storyline)."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/category/index",
            params=self.client_config.static_params,
        ).json()

    def get_quest_category(self, questCategoryId: int):
        """Returns a quest category by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/category/{questCategoryId}",
            params=self.client_config.static_params,
        ).json()

    def get_quest_areas_index(self):
        """Returns an index of quest areas."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/area/index",
            params=self.client_config.static_params,
        ).json()

    def get_quest_area(self, questAreaId: int):
        """Returns a quest area by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/area/{questAreaId}",
            params=self.client_config.static_params,
        ).json()

    def get_quest_types_index(self):
        """Returns an index of quest types (such as PvP quests, raid quests, or account quests)."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/type/index",
            params=self.client_config.static_params,
        ).json()

    def get_quest_type(self, questTypeId: int):
        """Returns a quest type by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/quest/type/{questTypeId}",
            params=self.client_config.static_params,
        ).json()

    def get_realms_index(self):
        """Returns an index of realms."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/realm/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_realm(self, realmSlug: str):
        """Returns a single realm by slug."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/realm/{realmSlug}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_regions_index(self):
        """Returns an index of regions."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/region/index",
            params=self.client_config.dynamic_params,
        ).json()

    def get_region(self, regionId: int):
        """Returns a region by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/region/{regionId}",
            params=self.client_config.dynamic_params,
        ).json()

    def get_reputation_factions_index(self):
        """Returns an index of reputation factions."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/reputation-faction/index",
            params=self.client_config.static_params,
        ).json()

    def get_reputation_faction(self, reputationFactionId: int):
        """Returns a single reputation faction by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/reputation-faction/{reputationFactionId}",
            params=self.client_config.static_params,
        ).json()

    def get_reputation_tiers_index(self):
        """Returns an index of reputation tiers."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/reputation-tiers/index",
            params=self.client_config.static_params,
        ).json()

    def get_reputation_tiers(self, reputationTiersId: int):
        """Returns a single set of reputation tiers by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/reputation-tiers/{reputationTiersId}",
            params=self.client_config.static_params,
        ).json()

    def get_spell(self, spellId: int):
        """Returns a spell by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/spell/{spellId}",
            params=self.client_config.static_params,
        ).json()

    def get_spell_media(self, spellId: int):
        """Returns media for a spell by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/media/spell/{spellId}",
            params=self.client_config.static_params,
        ).json()

    def get_talents_index(self):
        """Returns an index of talents."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/talent/index",
            params=self.client_config.static_params,
        ).json()

    def get_talent(self, talentId: int):
        """Returns a talent by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/talent/{talentId}",
            params=self.client_config.static_params,
        ).json()

    def get_pvp_talents_index(self):
        """Returns an index of PvP talents."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-talent/index",
            params=self.client_config.static_params,
        ).json()

    def get_pvp_talent(self, pvpTalentId: int):
        """Returns a PvP talent by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/pvp-talent/{pvpTalentId}",
            params=self.client_config.static_params,
        ).json()

    def get_titles_index(self):
        """Returns an index of titles."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/title/index",
            params=self.client_config.static_params,
        ).json()

    def get_title(self, titleId: int):
        """Returns a title by ID."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/title/{titleId}",
            params=self.client_config.static_params,
        ).json()

    def get_wow_token_index(self):
        """Returns an index of titles."""
        return self.client.get(
            f"{self.client_config.host}/data/wow/token/index",
            params=self.client_config.dynamic_params,
        ).json()
