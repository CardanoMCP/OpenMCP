export class OpenMCPCardanoClient {
  constructor(public endpoint: string = 'http://localhost:8000') {}

  health(): { status: string } {
    return { status: 'ok' };
  }
} 