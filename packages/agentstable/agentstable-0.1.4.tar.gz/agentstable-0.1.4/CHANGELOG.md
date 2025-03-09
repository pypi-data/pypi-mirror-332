# Changelog

All notable changes to the AgentStable SDK will be documented in this file.

## [0.1.3] - 2023-05-07

### Added

- Enhanced component discovery functionality
- Direct imports of component discovery functions in the main package
- Integration of UI component discovery with action-based workflows
- Improved error handling for component discovery
- Updated examples demonstrating component discovery with Anthropic
- Expanded README documentation with component discovery examples
- Organized examples directory for better usability

### Fixed

- Fixed component discovery response handling
- Improved error resilience when services are unavailable
- Better handling of component format variations

## [0.1.2] - 2023-05-01

### Added

- Improved token usage tracking for streaming API calls
- Direct access to output token counts from Anthropic streaming responses
- Input token estimation for streaming responses
- Better token usage persistence in Redis sessions
- New ActionGenerator module for creating action schemas from natural language
- OpenAI and Anthropic implementations of the ActionGenerator
- Utility functions to convert schemas to action service format
- Example demonstrating how to create and use the ActionGenerator
- Conversational clarification workflow for action schema generation
- Simplified imports for direct usage from the main package
- Component discovery module for finding and using UI components
- Functions to search, retrieve, and format UI components from a discovery service
- Example script demonstrating component discovery functionality

### Fixed

- Removed redundant API calls for token usage tracking
- Fixed message ID handling in streaming responses
