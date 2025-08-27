import { OpenMCPCardanoClient } from '../../../../src/client/typescript/src/client';

test('health returns ok', () => {
  const c = new OpenMCPCardanoClient();
  expect(c.health().status).toBe('ok');
}); 