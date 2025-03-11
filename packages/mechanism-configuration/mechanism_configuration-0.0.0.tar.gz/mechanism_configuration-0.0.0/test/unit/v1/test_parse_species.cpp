#include <gtest/gtest.h>

#include <mechanism_configuration/v1/parser.hpp>

using namespace mechanism_configuration;

TEST(ParserBase, CanParseValidSpecies)
{
  v1::Parser parser;
  std::vector<std::string> extensions = { ".json", ".yaml" };
  for (auto& extension : extensions)
  {
    auto parsed = parser.Parse(std::string("v1_unit_configs/species/valid_species") + extension);
    EXPECT_TRUE(parsed);
    v1::types::Mechanism mechanism = *parsed;
    EXPECT_EQ(mechanism.species.size(), 3);

    EXPECT_EQ(mechanism.species[0].name, "A");
    EXPECT_EQ(mechanism.species[0].unknown_properties.size(), 1);
    EXPECT_EQ(mechanism.species[0].unknown_properties["__absolute tolerance"], "1.0000000000000001e-30");

    EXPECT_EQ(mechanism.species[1].name, "H2O2");
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties.size(), 6);
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties["HLC(298K) [mol m-3 Pa-1]"], 1.011596348);
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties["HLC exponential factor [K]"], 6340);
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties["diffusion coefficient [m2 s-1]"], 1.46e-05);
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties["N star"], 1.74);
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties["molecular weight [kg mol-1]"], 0.0340147);
    EXPECT_EQ(mechanism.species[1].optional_numerical_properties["density [kg m-3]"], 1000.0);
    EXPECT_EQ(mechanism.species[1].unknown_properties.size(), 1);
    EXPECT_EQ(mechanism.species[1].unknown_properties["__absolute tolerance"], "1e-10");

    EXPECT_EQ(mechanism.species[2].name, "aerosol stuff");
    EXPECT_EQ(mechanism.species[2].optional_numerical_properties.size(), 2);
    EXPECT_EQ(mechanism.species[2].optional_numerical_properties["molecular weight [kg mol-1]"], 0.5);
    EXPECT_EQ(mechanism.species[2].optional_numerical_properties["density [kg m-3]"], 1000.0);
    EXPECT_EQ(mechanism.species[2].unknown_properties.size(), 1);
    EXPECT_EQ(mechanism.species[2].unknown_properties["__absolute tolerance"], "9.9999999999999995e-21");
  }
}

TEST(ParserBase, DetectsDuplicateSpecies)
{
  v1::Parser parser;
  std::vector<std::string> extensions = { ".json", ".yaml" };
  for (auto& extension : extensions)
  {
    std::string file = std::string("v1_unit_configs/species/duplicate_species") + extension;
    auto parsed = parser.Parse(file);
    EXPECT_FALSE(parsed);
    EXPECT_EQ(parsed.errors.size(), 1);
    EXPECT_EQ(parsed.errors[0].first, ConfigParseStatus::DuplicateSpeciesDetected);
    for (auto& error : parsed.errors)
    {
      std::cout << error.second << " " << configParseStatusToString(error.first) << std::endl;
    }
  }
}

TEST(ParserBase, DetectsMissingRequiredKeys)
{
  v1::Parser parser;
  std::vector<std::string> extensions = { ".json", ".yaml" };
  for (auto& extension : extensions)
  {
    std::string file = std::string("v1_unit_configs/species/missing_required_key") + extension;
    auto parsed = parser.Parse(file);
    EXPECT_FALSE(parsed);
    EXPECT_EQ(parsed.errors.size(), 2);
    EXPECT_EQ(parsed.errors[0].first, ConfigParseStatus::RequiredKeyNotFound);
    EXPECT_EQ(parsed.errors[1].first, ConfigParseStatus::InvalidKey);
    for (auto& error : parsed.errors)
    {
      std::cout << error.second << " " << configParseStatusToString(error.first) << std::endl;
    }
  }
}

TEST(ParserBase, DetectsInvalidKeys)
{
  v1::Parser parser;
  std::vector<std::string> extensions = { ".json", ".yaml" };
  for (auto& extension : extensions)
  {
    std::string file = std::string("v1_unit_configs/species/invalid_key") + extension;
    auto parsed = parser.Parse(file);
    EXPECT_FALSE(parsed);
    EXPECT_EQ(parsed.errors.size(), 1);
    EXPECT_EQ(parsed.errors[0].first, ConfigParseStatus::InvalidKey);
    for (auto& error : parsed.errors)
    {
      std::cout << error.second << " " << configParseStatusToString(error.first) << std::endl;
    }
  }
}