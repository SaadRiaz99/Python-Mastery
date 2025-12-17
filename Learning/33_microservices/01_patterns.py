patterns = {
    'API Gateway': 'Single entry point for all clients',
    'Service Discovery': 'Dynamic service location',
    'Circuit Breaker': 'Prevent cascade failures',
    'Event Sourcing': 'Store events instead of state',
    'CQRS': 'Separate read and write models',
    'Saga': 'Distributed transactions',
    'Sidecar': 'Helper service alongside main service',
    'Ambassador': 'Proxy service for external resources',
}

for name, desc in patterns.items():
    print(f'{name}: {desc}')
